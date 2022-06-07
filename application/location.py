from domain import fail2banlog


def get_locations(log_file, add_unbaned):
    baned_ips = fail2banlog.get_baned_ips(log_file, add_unbaned)
