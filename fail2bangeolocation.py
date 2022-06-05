import argparse
import signal

from application.fail2banlog import analyze
from application.utils.python_utils import exit_signal_handler, get_interpreter_version
from crosscutting import strings, constants
from crosscutting.condition_messages import print_error, print_info
from presentation.utils.screen import clear_screen

if __name__ == '__main__':
    signal.signal(signal.SIGINT, exit_signal_handler)
    clear_screen()
    interpreter_version = get_interpreter_version()

    if interpreter_version == constants.REQUIRED_PYTHON_VERSION:
        parser = argparse.ArgumentParser(description="Shows geolocation stats from fail2ban log")
        parser.add_argument('-f', '--file', metavar='fail2ban_log', nargs='?', help="fail2ban log file")
        args = parser.parse_args()

        if args.file:
            log_file = args.file
        else:
            log_file = constants.DEFAULT_LOG_FILE

        print_info("fail2bangeolocation")

        analyze(log_file)
    else:
        print_error(f"{strings.REQUIRES_PYTHON} {constants.REQUIRED_PYTHON_VERSION}")
        exit(0)
