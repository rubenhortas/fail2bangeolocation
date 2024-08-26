from src.fail2bangeolocation.presentation.tag import Tag


def print_error(error: str):
    print(f"{Tag.error} {error}")


def print_exception(exception: str):
    print(f"{Tag.exception} {exception}")


def print_info(info: str):
    print(f"{Tag.info} {info}")
