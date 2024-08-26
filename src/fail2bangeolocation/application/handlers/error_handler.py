from src.fail2bangeolocation.crosscutting.condition_messages import print_error


def handle_error(error, exit_=False):
    print_error(error)

    if exit_:
        exit(1)
