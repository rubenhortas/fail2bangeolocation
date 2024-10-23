from fail2bangeolocation.presentation.tag import Tag


def print_error(error: str) -> None:
    print(f"{Tag.error} {error}")


def print_exception(exception: Exception) -> None:
    print(f"{Tag.exception} {exception}")


def print_info(info: str) -> None:
    print(f"{Tag.info} {info}")
