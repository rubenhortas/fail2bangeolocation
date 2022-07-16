from sys import version_info
from fail2bangeolocation.crosscutting import condition_messages, strings


def get_interpreter_version():
    major, minor, micro, release_level, serial = version_info
    return major


# noinspection PyUnusedLocal
def exit_signal_handler(signal, frame):
    condition_messages.print_info(strings.STOPPED)
    exit(0)
