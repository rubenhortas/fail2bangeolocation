from fail2bangeolocation.crosscutting.condition_messages import print_exception


def handle_exception(exception: Exception) -> None:
    print_exception(exception)
    exit(1)
