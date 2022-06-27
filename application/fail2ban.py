from application.utils.system import execute_command

FAIL2BAN_CLIENT = 'fail2ban-client'
BANNED = 'banned'
STATUS = 'status'


def get_banned_ips(server=None):
    if server is None:
        return _get_banned_ips()
    else:
        return _get_server_banned_ips(server)


def _get_banned_ips():
    output = execute_command(FAIL2BAN_CLIENT, BANNED)
    return _parse_banned_ips(output)


def _parse_banned_ips(service_banned_ips):
    ips = []

    for service in service_banned_ips:
        for service_name in service:
            ips.extend(service[service_name])

    return ips


def _get_server_banned_ips(server):
    output = execute_command(FAIL2BAN_CLIENT, STATUS, server)
    return _parse_server_banned_ips(output)


def _parse_server_banned_ips(output):
    # TODO
    return output
