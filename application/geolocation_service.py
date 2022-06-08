from application import geolocationdb, fail2banlog
from domain.CountryStats import CountryStats
from domain.Location import Location


def analyze(log_file, add_unbaned):
    baned_ips = fail2banlog.get_baned_ips(log_file, add_unbaned)
    locations = __get_locations(baned_ips)
    countries = get_stats(locations)


def get_stats(locations):
    countries_stats = {}

    for location in locations:
        country = location.get_country()
        city = location.get_city()

        if country in countries_stats:
            country_stats = countries_stats[country]
            country_stats.add_city(city)
        else:
            country_stats = CountryStats(country, city)
            countries_stats[country] = country_stats
    return []


def __get_locations(ips):
    locations = []

    for ip in ips:
        country_name, city_name = geolocationdb.get_geolocation_info(ip)
        location = Location(country_name, city_name)
        locations.append(location)

    return locations
