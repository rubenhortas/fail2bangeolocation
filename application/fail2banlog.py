import os
import re
from crosscutting import strings, constants
from crosscutting.condition_messages import print_info, print_error


def analyze(log_file):
    if os.path.exists(log_file):
        banned_ip_regex = re.compile(r"^.* (Found|Ban) \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$")
        unbanned_ip_regex = re.compile(r"^.* Unban \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$")
        banned_ips = {}

        print_info(f"{strings.ANALYZING}: {log_file}")

        log = open(log_file, 'r')
        lines = log.readlines()

        for line in lines:
            banned_ip = re.match(banned_ip_regex, line)

            if banned_ip:
                banned_ips.add(banned_ip)
            else:
                if constants.DISCARD_UNBANNED_IPS:
                    unbanned_ip = re.match(unbanned_ip_regex, line)

                    if unbanned_ip:
                        set.discard(unbanned_ip)

        # [sshd] Found 171.217.64.241
        # [sshd] Ban 171.217.64.241
        # [sshd] Restore Ban 1.202.77.126
        # [sshd] Unban 196.38.70.24

        # geo = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
    else:
        print_error(f"{log_file} {strings.DOES_NOT_EXISTS}")
