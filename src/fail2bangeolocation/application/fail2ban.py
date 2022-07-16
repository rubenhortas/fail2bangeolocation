import ast
import re

from fail2bangeolocation.application.utils.system import execute_command

FAIL2BAN_CLIENT = 'fail2ban-client'
BANNED = 'banned'
STATUS = 'status'


def get_banned_ips(server=None):
    if server is None:
        return _get_banned_ips()
    else:
        return _get_server_banned_ips(server)


def _get_banned_ips():
    command_stdout = execute_command(FAIL2BAN_CLIENT, BANNED)

    if command_stdout:
        return _parse_banned_ips(command_stdout)
    else:
        return []


def _parse_banned_ips(service_banned_ips):
    ips = []

    sbi = ast.literal_eval(service_banned_ips.decode('UTF-8'))

    for service in sbi:
        for service_name in service:
            ips.extend(service[service_name])

    return ips


def _get_server_banned_ips(server):
    command_stdout = execute_command(FAIL2BAN_CLIENT, STATUS, server)

    if command_stdout:
        return _parse_server_banned_ips(command_stdout)
    else:
        return []


def _parse_server_banned_ips(command_stdout):
    ips_regex = re.compile(r'(?P<ips>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}.*)')

    command_stdout_ips = ips_regex.findall(command_stdout.decode('UTF-8'))

    if command_stdout_ips:
        return str.split(command_stdout_ips[0])
    else:
        return []
