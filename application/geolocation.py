from tqdm import tqdm

from application import geolocationdb, fail2banlog, fail2ban
from crosscutting import strings
from crosscutting.condition_messages import print_info, print_error
from domain.Attempt import Attempt

NOT_FOUND = "Not found"


def analyze(fail2ban_output=None, server=None, log_file=None, add_unbanned=None, group_by_city=None):
    banned_ips = []

    if geolocationdb.is_online():
        if fail2ban_output is not None:
            banned_ips = fail2ban.get_banned_ips()
        elif server is not None:
            banned_ips = fail2ban.get_banned_ips(server)
        elif log_file is not None:
            banned_ips = fail2banlog.get_banned_ips(log_file, add_unbanned)

        print_info(f'{len(banned_ips)} {strings.IPS_FOUND}')

        if len(banned_ips) > 0:
            print_info(strings.GEOLOCATING_IPS)

            # locations, ips_not_found = _geolocate(banned_ips)
            # attempts = _get_attempts(locations)
            # sorted_attempts = _sort(attempts, group_by_city)
            #
            # print_info(strings.LOCATIONS)
            #
            # _print_attempts(sorted_attempts, group_by_city)
            # _print_not_found(ips_not_found)

            locations, ips_not_found = _geolocate(banned_ips)
            locations = _rename_unknown_locations(locations)
            failed_attempts = _get_failed_attempts(locations)
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
    failed_attempts = []

    for location in locations:
        exists = False

        for failed_attempt in failed_attempts:
            if failed_attempt.country == location[0]:
                failed_attempt.add_city(location[1])
                exists = True
                break

        if not exists:
            new_failed_attempt = Attempt(location[0])
            new_failed_attempt.add_city(location[1])
            failed_attempts.append(new_failed_attempt)

    return failed_attempts

# def _get_attempts(locations):
#     attempts = {}
#
#     for location in locations:
#         country = location.country
#         city = location.city
#
#         if country not in attempts:
#             attempts[country] = {city: 0}
#
#         if city not in attempts[country]:
#             (attempts[country])[city] = 0
#
#         (attempts[country])[city] = (attempts[country])[city] + 1
#
#     return attempts


# def _sort(attempts, group_by_city):
#     if group_by_city:
#         return _sort_by_city(attempts)
#     else:
#         return _sort_by_country(attempts)
#
#
# def _sort_by_country(attempts):
#     countries_totals = {}
#
#     for country in attempts:
#         country_total = 0
#
#         for city in attempts[country]:
#             country_total = country_total + (attempts[country])[city]
#
#         countries_totals[country] = country_total
#
#     country_totals_alphabetically_sorted = {k: v for k, v in
#                                             sorted(countries_totals.items(), key=lambda item: item[0], reverse=False)}
#     country_totals_sorted = {k: v for k, v in
#                              sorted(country_totals_alphabetically_sorted.items(), key=lambda item: item[1],
#                                     reverse=True)}
#
#     return country_totals_sorted
#
#
# def _sort_by_city(attempts):
#     attempts_sorted_by_city = {}
#     attempts_sorted_by_country = _sort_by_country(attempts)
#     result = {}
#
#     for country in attempts:
#         renamed_cities_attempts = {}
#
#         for k in attempts[country]:
#             if (k is None) or (k == NOT_FOUND):
#                 renamed_cities_attempts[strings.UNKNOWN] = (attempts[country])[k]
#             else:
#                 renamed_cities_attempts[k] = (attempts[country])[k]
#
#         attempts_sorted_by_cities_alphabetically = {k: v for k, v in
#                                                     sorted(renamed_cities_attempts.items(), key=lambda item: item[0],
#                                                            reverse=False)}
#
#         attempts_sorted_by_city[country] = {k: v for k, v in sorted(attempts_sorted_by_cities_alphabetically.items(),
#                                                                     key=lambda item: item[1], reverse=True)}
#
#     for country in attempts_sorted_by_country:
#         result[country] = attempts_sorted_by_city[country]
#
#     return result
#
#
# def _print_attempts(stats, group_by_city):
#     if group_by_city:
#         for country in stats:
#             country_total = 0
#
#             for city in stats[country]:
#                 country_total = country_total + (stats[country])[city]
#
#             messages.print_country(country, country_total)
#
#             for city in stats[country]:
#                 messages.print_city(city, (stats[country])[city])
#     else:
#         for country in stats:
#             messages.print_country(country, stats[country])


# def _print_not_found(ips):
#     messages.print_error(f'{strings.IPS_NOT_FOUND} {", ".join(ips)}')
