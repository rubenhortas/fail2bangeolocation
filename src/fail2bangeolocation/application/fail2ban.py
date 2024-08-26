import re

from src.fail2bangeolocation.application.utils.system import execute_command

_FAIL2BAN_CLIENT = 'fail2ban-client'
_BANNED = 'banned'
_STATUS = 'status'
_REGEX_IP = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')


def get_banned_ips(server: str = None) -> list:
    if server is None:
        command_stdout = execute_command(_FAIL2BAN_CLIENT, _BANNED)
    else:
        command_stdout = execute_command(_FAIL2BAN_CLIENT, _STATUS, server)

    if command_stdout:
        return _parse_banned_ips(command_stdout)
    else:
        return []


def _parse_banned_ips(command_stdout: bytes) -> list:
    return _REGEX_IP.findall(command_stdout.decode('UTF-8'))
