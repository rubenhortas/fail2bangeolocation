from collections import defaultdict
from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request

from tqdm import tqdm

from src.fail2bangeolocation.application import fail2ban, fail2banlog
from src.fail2bangeolocation.application.handlers.error_handler import handle_error
from src.fail2bangeolocation.application.reallyfreegeoip import URL, get_location
from src.fail2bangeolocation.crosscutting import strings
from src.fail2bangeolocation.crosscutting.condition_messages import print_info


def geolocate(fail2ban_output: bool = None, server: str = None, log_file: str = None, add_unbanned: bool = None,
              group_by_city: bool = None) -> None:
    # noinspection SpellCheckingInspection
    print_info('fail2bangeolocation')

    ips = []

    if _is_online():
        if fail2ban_output:
            ips = fail2ban.get_banned_ips()
        elif server:
            ips = fail2ban.get_banned_ips(server)
        elif log_file:
            ips = fail2banlog.get_banned_ips(log_file, add_unbanned)

        print_info(f"{len(ips)} {strings.IPS_FOUND}")

        if len(ips) > 0:
            print_info(strings.GEOLOCATING_IPS)

            locations, ips_not_found = _geolocate(ips)
            # grouped_locations = _group_locations(locations)
            # locations_sorted_by_country, locations_sorted_by_country_and_city = _sort(grouped_locations, group_by_city)
            #
            # print_info(strings.LOCATIONS)
            # _print_locations(locations_sorted_by_country, locations_sorted_by_country_and_city)
            #
            # if len(ips_not_found) > 0:
            #     _print_not_found(ips_not_found)


def _is_online():
    try:
        request = Request(
            url=URL,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        _ = urlopen(request).read()
        return True
    except HTTPError or URLError or OSError:
        handle_error(f"{URL} {strings.IS_NOT_REACHABLE}", True)


def _geolocate(ips: list) -> (dict, list):
    locations = defaultdict(list)
    ips_not_located = []

    for ip in tqdm(ips):
        country, city = get_location(ip)

        if country:
            if city:
                locations[country].append(city)
            else:
                locations[country].append(strings.UNKNOWN)
        else:
            ips_not_located.append(ip)

    return locations, ips_not_located


# def _group_locations(locations: list) -> dict:
#     countries = {}
#
#     for location in locations:
#         country = location[0]
#         city = location[1]
#
#         if country not in countries:
#             countries[country] = {city: 0}
#
#         if city not in countries[country]:
#             (countries[country])[city] = 0
#
#         (countries[country])[city] = (countries[country])[city] + 1
#
#     return countries
#
#
# def _sort(locations: dict, group_by_city: bool) -> (dict, dict):
#     if group_by_city:
#         return _sort_by_country_and_city(locations)
#     else:
#         return _sort_by_country(locations)
#
#
# def _sort_by_country_and_city(locations: dict) -> (dict, dict):
#     attempts_sorted_by_country = _sort_by_country(locations)[0]
#     attempts_sorted_by_city = {}
#
#     for country in locations:
#         attempts_sorted_by_city_alphabetically = {k: v for k, v in
#                                                   sorted(locations[country].items(), key=lambda item: item[0],
#                                                          reverse=False)}
#
#         attempts_sorted_by_city[country] = {k: v for k, v in sorted(attempts_sorted_by_city_alphabetically.items(),
#                                                                     key=lambda item: item[1], reverse=True)}
#
#     return attempts_sorted_by_country, attempts_sorted_by_city
#
#
# def _sort_by_country(locations: dict) -> (dict, None):
#     countries_totals = {}
#
#     for country in locations:
#         country_total = 0
#
#         for city in locations[country]:
#             country_total = country_total + (locations[country])[city]
#
#         countries_totals[country] = country_total
#
#     countries_totals_sorted_alphabetically = {k: v for k, v in
#                                               sorted(countries_totals.items(), key=lambda item: item[0], reverse=False)}
#     countries_totals_sorted_by_total = {k: v for k, v in
#                                         sorted(countries_totals_sorted_alphabetically.items(), key=lambda item: item[1],
#                                                reverse=True)}
#
#     return countries_totals_sorted_by_total, None
#
#
# def _print_locations(locations_sorted_by_country: dict, locations_sorted_by_country_and_city: dict | None) -> None:
#     for country in locations_sorted_by_country:
#         messages.print_country(country, locations_sorted_by_country[country])
#
#         if locations_sorted_by_country_and_city:
#             for city in locations_sorted_by_country_and_city[country]:
#                 messages.print_city(city, (locations_sorted_by_country_and_city[country])[city])
#
#
# def _print_not_found(ips: list) -> None:
#     messages.print_error(f"{strings.IPS_NOT_FOUND} {', '.join(ips)}")
