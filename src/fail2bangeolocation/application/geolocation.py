from tqdm import tqdm

from src.fail2bangeolocation.crosscutting.strings import UNKNOWN
from src.fail2bangeolocation.application import fail2ban, fail2banlog
from src.fail2bangeolocation.application.reallyfreegeoip import get_location, REALLYFREEGEOIP_URL
from src.fail2bangeolocation.application.utils.country import Country
from src.fail2bangeolocation.application.utils.url_utils import is_online
from src.fail2bangeolocation.crosscutting import strings
from src.fail2bangeolocation.crosscutting.condition_messages import print_info
from src.fail2bangeolocation.presentation import messages


def geolocate(fail2ban_output: bool = None, server: str = None, log_file: str = None, add_unbanned: bool = None,
              group_by_city: bool = False) -> None:
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
            grouped_locations_sorted = _sort_grouped_locations(grouped_locations, group_by_city)

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
        city = location[1] if location[1] else UNKNOWN

        if country not in grouped_locations:
            grouped_locations[country] = {city: 0}

        if city not in grouped_locations[country]:
            (grouped_locations[country])[city] = 0

        (grouped_locations[country])[city] = (grouped_locations[country])[city] + 1

    return grouped_locations


def _sort_grouped_locations(locations: dict, group_by_city: bool) -> list:
    countries = []

    for location in locations:
        countries.append(Country(location, locations[location], group_by_city))

    return sorted(countries, reverse=True)


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
