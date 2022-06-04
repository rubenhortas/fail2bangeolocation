from presentation.tag import Tag


def print_debug(msg):
    print("{0} {1}".format(Tag.debug, msg))


def print_error(msg):
    print("{0} {1}".format(Tag.error, msg))


def print_exception(msg):
    print("{0} {1}".format(Tag.exception, msg))


def print_warning(msg):
    print("{0} {1}".format(Tag.warning, msg))


def print_info(msg):
    print("{0} {1}".format(Tag.info, msg))
