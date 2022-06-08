from domain import fail2banlog, geolocation
from domain.IpInfo import IpInfo


def get_locations(log_file, add_unbaned):
    locations = []
    baned_ips = fail2banlog.get_baned_ips(log_file, add_unbaned)

    for ip in baned_ips:
        country, city = geolocation.get_geolocation_info(ip)
        ip_info = IpInfo(country, city)
        locations.append(ip_info)

    print(locations)
