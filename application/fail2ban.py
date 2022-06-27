import re

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
    command_output = execute_command(FAIL2BAN_CLIENT, STATUS, server)
    return _parse_server_banned_ips(command_output)


def _parse_server_banned_ips(command_output):
    ips_regex = re.compile(r'(?P<ips>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}.*)')

    command_output_ips = ips_regex.findall(command_output.decode('UTF-8'))

    if command_output_ips is not None:
        return str.split(command_output_ips[0])
    else:
        return None
