from crosscutting.condition_messages import print_error


def handle_error(err, ext):
    print_error(err.decode('UTF-8'))

    if ext:
        exit(1)
