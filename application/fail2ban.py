FAIL2BAN_CLIENT_BANNED_COMMAND = 'fail2ban-client banned'
FAIL2BAN_CLIENT_STATUS_COMMAND = 'fail2ban-client status'


def get_banned_ips(server=None):
    if server is None:
        return _get_banned_ips()
    else:
        return _get_server_banned_ips(server)


def _get_banned_ips():
    return []


def _get_server_banned_ips(server):
    return []
