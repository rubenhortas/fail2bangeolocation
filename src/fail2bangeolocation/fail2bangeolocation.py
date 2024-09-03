#!/usr/bin/env python3

import argparse
import signal

from src.fail2bangeolocation.application.handlers.signal_handler import handle_sigint
from src.fail2bangeolocation.application.geolocation import geolocate
from src.fail2bangeolocation.application.utils.python_utils import get_python_interpreter_version
from src.fail2bangeolocation.crosscutting import constants, strings
from src.fail2bangeolocation.crosscutting.condition_messages import print_error
from src.fail2bangeolocation.presentation.utils.screen import clear_screen

_FAIL2BAN_OPTION = 'fail2ban'
_LOG_OPTION = 'log'
_SERVER_OPTION = 'server'


def main():
    signal.signal(signal.SIGINT, handle_sigint)
    clear_screen()

    if get_python_interpreter_version() == constants.REQUIRED_PYTHON_VERSION:
        parser = argparse.ArgumentParser(description=f'{strings.DESCRIPTION}')
        parser.add_argument('-c', '--show-city', default=False, action='store_true', help=f'{strings.GROUP_BY_CITY}')
        subparsers = parser.add_subparsers(help=f'{strings.THESE_OPTIONS_ARE_MUTUALLY_EXCLUSIVE}')

        parser_output = subparsers.add_parser(_FAIL2BAN_OPTION, help=f'{strings.OUTPUT_OPTIONS_HELP}')
        parser_output.add_argument(_FAIL2BAN_OPTION, default=False, action='store_true',
                                   help=f'{strings.OUTPUT_OPTION_HELP}')

        parser_log = subparsers.add_parser(_LOG_OPTION, help=f'{strings.LOG_OPTIONS_HELP}')
        parser_log.add_argument(_LOG_OPTION, nargs=1, help=f'{strings.LOG_OPTION_HELP}')
        parser_log.add_argument('-u', '--add-unbanned', default=False, action='store_true',
                                help=f'{strings.UNBANNED_IPS_OPTION_HELP}')

        parser_server = subparsers.add_parser(_SERVER_OPTION, help=f'{strings.SERVER_OPTIONS_HELP}')
        parser_server.add_argument(_SERVER_OPTION, nargs=1, help=f'{strings.SERVER_OPTION_HELP}')

        args = parser.parse_args()

        if args.__contains__(_FAIL2BAN_OPTION):
            geolocate(fail2ban_output=True, group_by_city=args.show_city)
        elif args.__contains__(_LOG_OPTION):
            geolocate(log_file=args.log[0], add_unbanned=args.add_unbanned, group_by_city=args.show_city)
        elif args.__contains__(_SERVER_OPTION):
            geolocate(server=args.server[0], group_by_city=args.show_city)
        else:
            parser.print_help()
    else:
        print_error(f"{strings.REQUIRES_PYTHON} {constants.REQUIRED_PYTHON_VERSION}")
        exit(0)


if __name__ == '__main__':
    main()
