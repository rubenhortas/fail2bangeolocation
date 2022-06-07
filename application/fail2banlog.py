import os
import re

from application.handlers.error_handler import handle_error
from application.handlers.exception_handler import handle_exception
from crosscutting import strings
from crosscutting.condition_messages import print_info


def analyze(log_file, add_unbaned):
    try:
        if os.path.exists(log_file):
            if os.path.isfile(log_file):
                print_info(f"{strings.ANALYZING}: {log_file}")

                ips = __get_ips(log_file, add_unbaned)
                locations = __get_locations(ips)
            else:
                handle_error(f"{log_file} {strings.IS_NOT_A_FILE}", True)
        else:
            handle_error(f"{log_file} {strings.DOES_NOT_EXISTS}", True)
    except Exception as e:
        handle_exception(e)


def __get_ips(log_file, add_unbaned):
    banned_ip_regex = re.compile(r'^.*\s(Found|Ban)\s(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*$')
    unbanned_ip_regex = re.compile(r'^.*\sUnban\s(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*$')
    banned_ips = set()

    log = open(log_file, 'r')
    lines = log.readlines()

    for line in lines:
        match = banned_ip_regex.search(line)

        if match:
            banned_ips.add(match.group("ip"))
        else:
            match = unbanned_ip_regex.search(line)

            if match:
                if add_unbaned:
                    banned_ips.add(match.group("ip"))
                else:
                    banned_ips.discard(match.group("ip"))

    return banned_ips


def __get_locations(ips):
    locations = dict()

    for ip in ips:
        pass

    return locations
