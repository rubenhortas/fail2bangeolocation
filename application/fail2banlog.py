import os
import re
from crosscutting import strings, constants
from crosscutting.condition_messages import print_info, print_error


def analyze(log_file, add_unbaned):
    if os.path.exists(log_file):
        banned_ip_regex = re.compile(r'^.*\s(Found|Ban)\s(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*$')
        unbanned_ip_regex = re.compile(r'^.*\sUnban\s(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*$')
        banned_ips = set()

        print_info(f"{strings.ANALYZING}: {log_file}")

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

    else:
        print_error(f"{log_file} {strings.DOES_NOT_EXISTS}")
