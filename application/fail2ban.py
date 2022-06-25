from application.utils.system import execute_command

FAIL2BAN_CLIENT_BANNED_COMMAND = 'fail2ban-client banned'
FAIL2BAN_CLIENT_STATUS_COMMAND = 'fail2ban-client status'


def get_banned_ips(server=None):
    if server is None:
        return _get_banned_ips()
    else:
        return _get_server_banned_ips(server)


def _get_banned_ips():
    output = execute_command(FAIL2BAN_CLIENT_BANNED_COMMAND)
    return _parse_banned_ips(output)


def _parse_banned_ips(service_banned_ips):
    ips = []

    for service in service_banned_ips:
        ips.extend(service_banned_ips[service])

    return ips


def _get_server_banned_ips(server):
    output = execute_command(f'{FAIL2BAN_CLIENT_BANNED_COMMAND} {server}')
    return _parse_server_banned_ips(output)


def _parse_server_banned_ips(output):
    # TODO
    return []
