from application import geolocationdb, fail2banlog
from domain.Location import Location


def analyze(log_file, add_unbaned):
    baned_ips = fail2banlog.get_baned_ips(log_file, add_unbaned)
    locations = __get_locations(baned_ips)
    stats = get_stats(locations)


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


def __get_locations(ips):
    locations = []

    for ip in ips:
        country_name, city_name = geolocationdb.get_geolocation_info(ip)
        location = Location(country_name, city_name)
        locations.append(location)

    return locations
