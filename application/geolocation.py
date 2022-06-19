from tqdm import tqdm

from application import geolocationdb, fail2banlog
from crosscutting import strings
from crosscutting.condition_messages import print_info
from domain.Location import Location
from presentation import messages

NOT_FOUND = "Not found"


def analyze(log_file, add_unbaned, group_by_city):
    baned_ips = fail2banlog.get_baned_ips(log_file, add_unbaned)

    print_info(f'{len(baned_ips)} {strings.IPS_FOUND}')
    print_info(strings.GEOLOCATING_IPS)

    locations, ips_not_found = _get_locations(baned_ips)
    attempts = _get_attempts(locations)
    sorted_attempts = _sort(attempts, group_by_city)

    print_info(strings.LOCATIONS)

    _print_attempts(sorted_attempts, group_by_city)
    _print_not_found(ips_not_found)


def _get_locations(ips):
    locations = []
    ips_not_found = []

    for ip in tqdm(ips):
        country_name, city_name = geolocationdb.get_geolocation_info(ip)

        if country_name and (country_name != NOT_FOUND):
            location = Location(country_name, city_name)
            locations.append(location)
        else:
            ips_not_found.append(ip)

    return locations, ips_not_found


def _get_attempts(locations):
    attempts = {}

    for location in locations:
        country = location.get_country()
        city = location.get_city()

        if country not in attempts:
            attempts[country] = {city: 0}

        if city not in attempts[country]:
            (attempts[country])[city] = 0

        (attempts[country])[city] = (attempts[country])[city] + 1

    return attempts


def _sort(attempts, group_by_city):
    if group_by_city:
        return _sort_by_city(attempts)
    else:
        return _sort_by_country(attempts)


def _sort_by_country(attempts):
    countries_totals = {}

    for country in attempts:
        country_total = 0

        for city in attempts[country]:
            country_total = country_total + (attempts[country])[city]

        countries_totals[country] = country_total

    country_totals_alphabetically_sorted = {k: v for k, v in
                                            sorted(countries_totals.items(), key=lambda item: item[0], reverse=False)}
    country_totals_sorted = {k: v for k, v in
                             sorted(country_totals_alphabetically_sorted.items(), key=lambda item: item[1],
                                    reverse=True)}

    return country_totals_sorted


def _sort_by_city(attempts):
    attempts_sorted_by_country = _sort_by_country(attempts)
    attempts_sorted_by_city = {}
    result = {}

    for country in attempts:
        sorted_cities = {}

        attempts_sorted_by_cities_alphabetically = {k: v for k, v in sorted(attempts[country].items(),
                                                                            key=lambda item: item[0], reverse=False)}

        for city in sorted(attempts_sorted_by_cities_alphabetically.items(), key=lambda item: item[1], reverse=True):
            if (city[0] is None) or (city[0] == NOT_FOUND):
                sorted_cities[strings.UNKNOWN] = city[1]
            else:
                sorted_cities[city[0]] = city[1]

        attempts_sorted_by_city[country] = sorted_cities

    for country in attempts_sorted_by_country:
        result[country] = attempts_sorted_by_city[country]

    return result


def _print_attempts(stats, group_by_city):
    if group_by_city:
        for country in stats:
            messages.print_country(country)

            for city in stats[country]:
                messages.print_city(city, (stats[country])[city])
    else:
        for country in stats:
            messages.print_country(country, stats[country])


def _print_not_found(ips):
    messages.print_error(f'{strings.IPS_NOT_FOUND} {", ".join(ips)}')