from application import geolocationdb, fail2banlog
from crosscutting import strings
from domain.Location import Location


def analyze(log_file, add_unbaned, group_by_city):
    baned_ips = fail2banlog.get_baned_ips(log_file, add_unbaned)
    locations = __get_locations(baned_ips)
    stats = get_stats(locations)
    sorted_stats = sort(stats, group_by_city)
    print_stats(sorted_stats, group_by_city)


def get_stats(locations):
    stats = {}

    for location in locations:
        country = location.get_country()
        city = location.get_city()

        if country not in stats:
            stats[country] = {city: 0}

        if city not in stats[country]:
            (stats[country])[city] = 0

        (stats[country])[city] = (stats[country])[city] + 1

    return stats


def sort(stats, group_by_city):
    if group_by_city:
        return __sort_by_city(stats)
    else:
        return __sort_by_country(stats)


def __get_locations(ips):
    locations = []

    for ip in ips:
        country_name, city_name = geolocationdb.get_geolocation_info(ip)

        if country_name:
            location = Location(country_name, city_name)
            locations.append(location)

    return locations


def __sort_by_country(stats):
    country_totals = {}
    country_totals_sorted = {}

    for country in stats:
        country_total = 0

        for city in stats[country]:
            country_total = country_total + (stats[country])[city]

        country_totals[country] = country_total

    for total in sorted(country_totals.items(), key=lambda x: x[1], reverse=True):
        country_totals_sorted[total[0]] = total[1]

    return country_totals_sorted


def __sort_by_city(stats):
    stats_sorted_by_country = __sort_by_country(stats)
    stats_sorted_by_city = {}
    result = {}

    for country in stats:
        sorted_cities = {}

        for city in sorted(stats[country].items(), key=lambda x: x[1], reverse=True):
            if city[0] is None:
                sorted_cities[strings.UNKNOWN] = city[1]
            else:
                sorted_cities[city[0]] = city[1]

        stats_sorted_by_city[country] = sorted_cities

    for country in stats_sorted_by_country:
        result[country] = stats_sorted_by_city[country]

    return result


def print_stats(stats, group_by_city):
    if group_by_city:
        for country in stats:
            print(f"{country}")

            for city in stats[country]:
                print(f"\t{city}: {(stats[country])[city]}")
    else:
        for country in stats:
            print(f"{country}: {stats[country]}")
