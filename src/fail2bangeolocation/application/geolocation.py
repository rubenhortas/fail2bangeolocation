from tqdm import tqdm

from fail2bangeolocation.application import geolocationdb
from fail2bangeolocation.application import fail2ban, fail2banlog
from fail2bangeolocation.crosscutting import strings
from fail2bangeolocation.crosscutting.condition_messages import print_info, print_error
from fail2bangeolocation.presentation import messages

NOT_FOUND = "Not found"


def analyze(fail2ban_output=None, server=None, log_file=None, add_unbanned=None, group_by_city=None):
    banned_ips = []

    print_info('fail2bangeolocation')

    if geolocationdb.is_online():
        if fail2ban_output is not None:
            banned_ips = fail2ban.get_banned_ips()
        elif server is not None:
            banned_ips = fail2ban.get_banned_ips(server)
        elif log_file is not None:
            banned_ips = fail2banlog.get_banned_ips(log_file, add_unbanned)

        print_info(f"{len(banned_ips)} {strings.IPS_FOUND}")

        if len(banned_ips) > 0:
            print_info(strings.GEOLOCATING_IPS)

            locations, ips_not_found = _geolocate(banned_ips)
            locations = _rename_unknown_locations(locations)
            failed_attempts = _get_failed_attempts(locations)
            failed_attempts_sorted_by_country, failed_attempts_sorted_by_country_and_city = _sort(failed_attempts,
                                                                                                  group_by_city)

            print_info(strings.LOCATIONS)
            _print_attempts(failed_attempts_sorted_by_country, failed_attempts_sorted_by_country_and_city)

            if len(ips_not_found) > 0:
                _print_not_found(ips_not_found)
    else:
        print_error(f"{geolocationdb.GEOLOCATIONDB_URL} {strings.IS_NOT_REACHABLE}")
        exit(0)


def _geolocate(ips):
    locations = []
    ips_not_found = []

    for ip in tqdm(ips):
        country_name, city_name = geolocationdb.get_geolocation_info(ip)

        if country_name and (country_name != NOT_FOUND):
            locations.append((country_name, city_name))
        else:
            ips_not_found.append(ip)

    return locations, ips_not_found


def _rename_unknown_locations(locations):
    renamed_locations = []

    for location in locations:
        if location[1] is None or location[1] == NOT_FOUND:
            renamed_locations.append((location[0], strings.UNKNOWN))
        else:
            renamed_locations.append(location)

    return renamed_locations


def _get_failed_attempts(locations):
    failed_attempts = {}

    for location in locations:
        country = location[0]
        city = location[1]

        if country not in failed_attempts:
            failed_attempts[country] = {city: 0}

        if city not in failed_attempts[country]:
            (failed_attempts[country])[city] = 0

        (failed_attempts[country])[city] = (failed_attempts[country])[city] + 1

    return failed_attempts


def _sort(attempts, group_by_city):
    if group_by_city:
        return _sort_by_country_and_city(attempts)
    else:
        return _sort_by_country(attempts)


def _sort_by_country_and_city(attempts):
    attempts_sorted_by_country = _sort_by_country(attempts)[0]
    attempts_sorted_by_city = {}

    for country in attempts:
        attempts_sorted_by_city_alphabetically = {k: v for k, v in
                                                  sorted(attempts[country].items(), key=lambda item: item[0],
                                                         reverse=False)}

        attempts_sorted_by_city[country] = {k: v for k, v in sorted(attempts_sorted_by_city_alphabetically.items(),
                                                                    key=lambda item: item[1], reverse=True)}

    return attempts_sorted_by_country, attempts_sorted_by_city


def _sort_by_country(attempts):
    countries_totals = {}

    for country in attempts:
        country_total = 0

        for city in attempts[country]:
            country_total = country_total + (attempts[country])[city]

        countries_totals[country] = country_total

    countries_totals_sorted_alphabetically = {k: v for k, v in
                                              sorted(countries_totals.items(), key=lambda item: item[0], reverse=False)}
    countries_totals_sorted_by_total = {k: v for k, v in
                                        sorted(countries_totals_sorted_alphabetically.items(), key=lambda item: item[1],
                                               reverse=True)}

    return countries_totals_sorted_by_total, None


def _print_attempts(attempts_sorted_by_country, attempts_sorted_by_country_and_city):
    for country in attempts_sorted_by_country:
        messages.print_country(country, attempts_sorted_by_country[country])

        if attempts_sorted_by_country_and_city:
            for city in attempts_sorted_by_country_and_city[country]:
                messages.print_city(city, (attempts_sorted_by_country_and_city[country])[city])


def _print_not_found(ips):
    messages.print_error(f"{strings.IPS_NOT_FOUND} {', '.join(ips)}")
