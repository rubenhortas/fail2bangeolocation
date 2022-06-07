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
        parser.add_argument('log', nargs=1, help="fail2ban log file")
        parser.add_argument('-u', '--add-unbaned', default=False, action='store_true', help="add unbaned ips")
        args = parser.parse_args()

        print_info("fail2bangeolocation")

        analyze(args.log[0], args.add_unbaned)
    else:
        print_error(f"{strings.REQUIRES_PYTHON} {constants.REQUIRED_PYTHON_VERSION}")
        exit(0)
