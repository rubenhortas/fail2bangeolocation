from tqdm import tqdm

from fail2bangeolocation.crosscutting.strings import UNKNOWN
from fail2bangeolocation.domain import fail2ban, fail2banlog
from fail2bangeolocation.domain.country import Country
from fail2bangeolocation.domain.utils.url_utils import is_online
from fail2bangeolocation.infrastructure.reallyfreegeoip import get_location, REALLYFREEGEOIP_URL


def get_ips(fail2ban_output: bool = None, server: str = None, log_file: str = None, add_unbanned: bool = None) -> list:
    ips = []

    if is_online(REALLYFREEGEOIP_URL):
        if fail2ban_output:
            ips = fail2ban.get_banned_ips()
        elif server:
            ips = fail2ban.get_banned_ips(server)
        elif log_file:
            ips = fail2banlog.get_banned_ips(log_file, add_unbanned)

        return ips


def locate(ips: list, group_by_city: bool) -> (list, list):
    locations, ips_not_located = _get_locations(ips)
    grouped_locations = _group_locations(locations)

    return _sort_grouped_locations(grouped_locations, group_by_city), ips_not_located


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
