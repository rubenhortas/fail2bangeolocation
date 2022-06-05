import argparse
import os
import signal
from application.utils.python_utils import exit_signal_handler
from application.utils.python_utils import get_interpreter_version
from crosscutting import strings
from crosscutting.condition_messages import print_error, print_info
from crosscutting.constants import REQUIRED_PYTHON_VERSION
from presentation.utils.screen import clear_screen

if __name__ == '__main__':
    signal.signal(signal.SIGINT, exit_signal_handler)
    clear_screen()
    interpreter_version = get_interpreter_version()

    if interpreter_version == REQUIRED_PYTHON_VERSION:
        parser = argparse.ArgumentParser(description="Shows geolocation stats from fail2ban log")
        parser.add_argument('-f', '--file', metavar='fail2ban_log', nargs='?', help="fail2ban log file")
        args = parser.parse_args()

        if args.file:
            log_file = args.file
        else:
            log_file = '/var/log/fail2banlog'

        print_info("fail2bangeolocation")

        if os.path.exists(log_file):
            print_info(f"{strings.ANALYZING}: {log_file}")
        else:
            print_error(f"{log_file} {strings.DOES_NOT_EXISTS}")
    else:
        print_error(f"{strings.REQUIRES_PYTHON} {REQUIRED_PYTHON_VERSION}")
        exit(0)
