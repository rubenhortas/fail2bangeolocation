from src.fail2bangeolocation.presentation.tag import Tag


def print_error(msg: str):
    print(f"{Tag.error} {msg}")


def print_exception(msg: str):
    print(f"{Tag.exception} {msg}")


def print_info(msg: str):
    print(f"{Tag.info} {msg}")
