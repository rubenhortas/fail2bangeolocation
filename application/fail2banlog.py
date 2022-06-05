import os
from crosscutting import strings
from crosscutting.condition_messages import print_info, print_error


def analyze(log_file):
    if os.path.exists(log_file):
        print_info(f"{strings.ANALYZING}: {log_file}")

        log = open(log_file, 'r')
        # geo = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
    else:
        print_error(f"{log_file} {strings.DOES_NOT_EXISTS}")
