from presentation.tag import Tag


def print_debug(msg):
    print(f"{Tag.debug} {msg}")


def print_error(msg):
    print(f"{Tag.error} {msg}")


def print_exception(msg):
    print(f"{Tag.exception} {msg}")


def print_warning(msg):
    print(f"{Tag.warning} {msg}")


def print_info(msg):
    print(f"{Tag.info} {msg}")
