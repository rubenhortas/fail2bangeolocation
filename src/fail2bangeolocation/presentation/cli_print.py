from typing import List

from colorama import Style, Fore

from fail2bangeolocation.crosscutting import strings
from fail2bangeolocation.domain.country import Country


def print_locations(locations: List[Country], print_cities: bool) -> None:
    for location in locations:
        _print_country(location, print_cities)


def print_unlocated_ips(ips: list) -> None:
    print(f"{Style.BRIGHT}{Fore.RED}(!){Style.RESET_ALL} {strings.IPS_NOT_LOCATED} {', '.join(ips)}")


def _print_country(country: Country, print_cities) -> None:
    print(f"{Style.BRIGHT}{Fore.GREEN}{country.name}{Style.RESET_ALL}: {country.total}")

    if print_cities:
        for city in country.cities:
            print(f"\t{Style.BRIGHT}{Fore.YELLOW}{city}{Style.RESET_ALL}: {country.cities[city]}")
