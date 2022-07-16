from fail2bangeolocation.presentation.tag import Tag


def print_error(msg):
    print(f"{Tag.error} {msg}")


def print_exception(msg):
    print(f"{Tag.exception} {msg}")


def print_info(msg):
    print(f"{Tag.info} {msg}")
