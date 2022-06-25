import argparse
import signal

from application.geolocation import analyze
from application.utils.python_utils import exit_signal_handler, get_interpreter_version
from crosscutting import strings, constants
from crosscutting.condition_messages import print_error, print_info
from presentation.utils.screen import clear_screen

OUTPUT_OPTION = 'output'
LOG_OPTION = 'log'
SERVER_OPTION = 'server'

if __name__ == '__main__':
    signal.signal(signal.SIGINT, exit_signal_handler)
    clear_screen()
    interpreter_version = get_interpreter_version()

    if interpreter_version == constants.REQUIRED_PYTHON_VERSION:
        parser = argparse.ArgumentParser(description=f'{strings.DESCRIPTION}')
        parser.add_argument('-c', '--show-city', default=False, action='store_true', help=f'{strings.GROUP_BY_CITY}')
        subparsers = parser.add_subparsers(help=f'{strings.THIS_OPTIONS_ARE_MUTUALLY_EXCLUSIVE}')

        parser_output = subparsers.add_parser(OUTPUT_OPTION, help=f'{strings.OUTPUT_OPTIONS_HELP}')
        parser_output.add_argument(OUTPUT_OPTION, default=False, action='store_true',
                                   help=f'{strings.OUTPUT_OPTION_HELP}')

        parser_log = subparsers.add_parser(LOG_OPTION, help=f'{strings.LOG_OPTIONS_HELP}')
        parser_log.add_argument(LOG_OPTION, nargs=1, help=f'{strings.LOG_OPTION_HELP}')
        parser_log.add_argument('-u', '--add-unbaned', default=False, action='store_true',
                                help=f'{strings.UNBANNED_IPS_OPTION_HELP}')

        parser_server = subparsers.add_parser(SERVER_OPTION, help=f'{strings.SERVER_OPTIONS_HELP}')
        parser_server.add_argument(SERVER_OPTION, nargs=1, help=f'{strings.SERVER_OPTION_HELP}')

        args = parser.parse_args()

        print_info('fail2bangeolocation')

        if args.__contains__(OUTPUT_OPTION):
            print_info(f'output!')
        elif args.__contains__(LOG_OPTION):
            analyze(args.log[0], args.add_unbaned, args.show_city)
        elif args.__contains__(SERVER_OPTION):
            print_info(f'server {args.server[0]}! ')
    else:
        print_error(f'{strings.REQUIRES_PYTHON} {constants.REQUIRED_PYTHON_VERSION}')
        exit(0)
