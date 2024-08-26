from fail2bangeolocation.crosscutting import condition_messages, strings


# noinspection PyUnusedLocal
def handle_sigint(signal, frame):
    condition_messages.print_info(strings.STOPPED)

    exit(0)