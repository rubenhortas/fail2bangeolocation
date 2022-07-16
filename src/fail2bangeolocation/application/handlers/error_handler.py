from fail2bangeolocation.crosscutting.condition_messages import print_error


def handle_error(err, ext=False):
    print_error(err)

    if ext:
        exit(1)
