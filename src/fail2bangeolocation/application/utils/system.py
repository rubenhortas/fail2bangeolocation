from fail2bangeolocation.crosscutting import strings
from fail2bangeolocation.crosscutting.condition_messages import print_info, print_error

import subprocess


def execute_command(command, *args):
    subprocess_command = [command]
    subprocess_command.extend(args)

    print_info(f"{strings.EXECUTING} {command} {' '.join(args)}")

    try:
        result = subprocess.run(subprocess_command, stdout=subprocess.PIPE)
        return result.stdout
    except Exception as e:
        print_error(e)
        return None
