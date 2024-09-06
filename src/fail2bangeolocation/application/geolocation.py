from tqdm import tqdm

from fail2bangeolocation.application.utils.url_utils import is_online
from fail2bangeolocation.presentation import messages
from src.fail2bangeolocation.application import fail2ban, fail2banlog
from src.fail2bangeolocation.application.reallyfreegeoip import get_location, REALLYFREEGEOIP_URL
from src.fail2bangeolocation.crosscutting import strings
from src.fail2bangeolocation.crosscutting.condition_messages import print_info


def geolocate(fail2ban_output: bool = None, server: str = None, log_file: str = None, add_unbanned: bool = None,
              group_by_city: bool = None) -> None:
    # noinspection SpellCheckingInspection
    print_info('fail2bangeolocation')

    ips = []

    if is_online(REALLYFREEGEOIP_URL):
        if fail2ban_output:
            ips = fail2ban.get_banned_ips()
        elif server:
            ips = fail2ban.get_banned_ips(server)
        elif log_file:
            print_info(f"{strings.ANALYZING}: {log_file}")
            ips = fail2banlog.get_banned_ips(log_file, add_unbanned)

        print_info(f"{len(ips)} {strings.IPS_FOUND}")

        if len(ips) > 0:
            print_info(strings.LOCATING_IPS)

            locations, ips_not_located = _get_locations(ips)
            grouped_locations = _group_locations(locations)
            grouped_locations_sorted = _sort_grouped_locations(grouped_locations)

            print_info(strings.LOCATIONS)

            # _print_locations(locations_sorted_by_country, locations_sorted_by_country_and_city)
            #
            if ips_not_located:
                _print_not_located(ips_not_located)


def _get_locations(ips: list) -> (str, str):
    locations = []
    ips_not_located = []

    for ip in tqdm(ips):
        country, city = get_location(ip)

        if country:
            locations.append((country, city))
        else:
            ips_not_located.append(ip)

    return locations, ips_not_located


def _group_locations(locations: list) -> dict:
    grouped_locations = dict({})

    for location in locations:
        country = location[0]
        city = location[1] if location[1] else 'Unknown'

        if country not in grouped_locations:
            grouped_locations[country] = {city: 0}

        if city not in grouped_locations[country]:
            (grouped_locations[country])[city] = 0

        (grouped_locations[country])[city] = (grouped_locations[country])[city] + 1

    return grouped_locations


def _sort_grouped_locations(locations: dict) -> dict:
    # Sort by country alphabetically
    sorted_dict = {k: v for k, v in sorted(locations.items(), key=lambda item: item[0], reverse=False)}

    for country, cities in sorted_dict:
        sorted_dict[country] = {k: v for k, v in sorted(cities.items(), key=lambda item: item[0], reverse=False)}
        sorted_dict[country] = {k: v for k, v in sorted(cities.items(), key=lambda item: item[1], reverse=False)}

    return sorted_dict


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
def _print_not_located(ips: list) -> None:
    messages.print_error(f"{strings.IPS_NOT_LOCATED} {', '.join(ips)}")
