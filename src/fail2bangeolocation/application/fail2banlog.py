import re

from src.fail2bangeolocation.application.handlers.exception_handler import handle_exception
from src.fail2bangeolocation.crosscutting import strings
from src.fail2bangeolocation.crosscutting.condition_messages import print_info

_REGEX_BANNED_IPS = re.compile(r'^.*\s(Found|Ban)\s(?P<ip>(\d{1,3}.){3}\d{1,3}).*$')
_REGEX_UNBANNED_IPS = re.compile(r'^.*\sUnban\s(?P<ip>(\d{1,3}.){3}\d{1,3}).*$')


def get_banned_ips(log_file, add_unbanned):
    banned_ips = set()

    try:
        with open(log_file, mode='r') as log:
            print_info(f"{strings.ANALYZING}: {log_file}")

            for line in log:
                match = _REGEX_BANNED_IPS.search(line)

                if match:
                    banned_ips.add(match.group('ip'))
                else:
                    match = _REGEX_UNBANNED_IPS.search(line)

                    if match:
                        if add_unbanned:
                            banned_ips.add(match.group('ip'))
                        else:
                            banned_ips.discard(match.group('ip'))
    except FileNotFoundError as file_not_found_error:
        handle_exception(file_not_found_error)
    except PermissionError as permission_error:
        handle_exception(permission_error)
    except OSError as os_error:
        handle_exception(os_error)

    return list(banned_ips)
