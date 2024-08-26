import ast
import re

from src.fail2bangeolocation.application.utils.system import execute_command

_FAIL2BAN_CLIENT = 'fail2ban-client'
_BANNED = 'banned'
_STATUS = 'status'
_REGEX_IP = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')


def get_banned_ips(server=None) -> list:
    if server is None:
        return _get_banned_ips()
    else:
        return _get_server_banned_ips(server)


def _get_banned_ips() -> list:
    command_stdout = execute_command(_FAIL2BAN_CLIENT, _BANNED)

    if command_stdout:
        return _parse_banned_ips(command_stdout)
    else:
        return []


def _parse_banned_ips(service_banned_ips: bytes) -> list:
    ips = []
    services = ast.literal_eval(service_banned_ips.decode('UTF-8'))

    for service in services:
        for service_name in service:
            ips.extend(service[service_name])

    return ips


def _get_server_banned_ips(server) -> list:
    command_stdout = execute_command(_FAIL2BAN_CLIENT, _STATUS, server)

    if command_stdout:
        return _parse_server_banned_ips(command_stdout)
    else:
        return []


def _parse_server_banned_ips(command_stdout) -> list:
    return _REGEX_IP.findall(command_stdout.decode('UTF-8'))
