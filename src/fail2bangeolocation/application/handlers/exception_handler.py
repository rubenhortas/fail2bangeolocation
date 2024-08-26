from src.fail2bangeolocation.crosscutting.condition_messages import print_exception


def handle_exception(exception: str) -> None:
    print_exception(exception)
    exit(1)
