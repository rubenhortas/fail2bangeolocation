from fail2bangeolocation.crosscutting.condition_messages import print_error


def handle_error(error: str, exit_: bool = False) -> None:
    print_error(error)

    if exit_:
        exit(1)
