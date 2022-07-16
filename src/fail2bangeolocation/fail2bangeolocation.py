#!/usr/bin/env python3

import argparse
import signal

from fail2bangeolocation.application.geolocation import analyze
from fail2bangeolocation.application.utils.python import exit_signal_handler, get_interpreter_version
from fail2bangeolocation.crosscutting import constants, strings
from fail2bangeolocation.crosscutting.condition_messages import print_error
from fail2bangeolocation.presentation.utils.screen import clear_screen

FAIL2BAN_OPTION = 'fail2ban'
LOG_OPTION = 'log'
SERVER_OPTION = 'server'


def main():
    signal.signal(signal.SIGINT, exit_signal_handler)
    clear_screen()
    interpreter_version = get_interpreter_version()

    if interpreter_version == constants.REQUIRED_PYTHON_VERSION:
        parser = argparse.ArgumentParser(description=f'{strings.DESCRIPTION}')
        parser.add_argument('-c', '--show-city', default=False, action='store_true', help=f'{strings.GROUP_BY_CITY}')
        subparsers = parser.add_subparsers(help=f'{strings.THESE_OPTIONS_ARE_MUTUALLY_EXCLUSIVE}')

        parser_output = subparsers.add_parser(FAIL2BAN_OPTION, help=f'{strings.OUTPUT_OPTIONS_HELP}')
        parser_output.add_argument(FAIL2BAN_OPTION, default=False, action='store_true',
                                   help=f'{strings.OUTPUT_OPTION_HELP}')

        parser_log = subparsers.add_parser(LOG_OPTION, help=f'{strings.LOG_OPTIONS_HELP}')
        parser_log.add_argument(LOG_OPTION, nargs=1, help=f'{strings.LOG_OPTION_HELP}')
        parser_log.add_argument('-u', '--add-unbanned', default=False, action='store_true',
                                help=f'{strings.UNBANNED_IPS_OPTION_HELP}')

        parser_server = subparsers.add_parser(SERVER_OPTION, help=f'{strings.SERVER_OPTIONS_HELP}')
        parser_server.add_argument(SERVER_OPTION, nargs=1, help=f'{strings.SERVER_OPTION_HELP}')

        args = parser.parse_args()

        if args.__contains__(FAIL2BAN_OPTION):
            analyze(fail2ban_output=True, group_by_city=args.show_city)
        elif args.__contains__(LOG_OPTION):
            analyze(log_file=args.log[0], add_unbanned=args.add_unbanned, group_by_city=args.show_city)
        elif args.__contains__(SERVER_OPTION):
            analyze(server=args.server[0], group_by_city=args.show_city)
        else:
            parser.print_help()
    else:
        print_error(f"{strings.REQUIRES_PYTHON} {constants.REQUIRED_PYTHON_VERSION}")
        exit(0)


if __name__ == '__main__':
    main()
