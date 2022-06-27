from crosscutting import strings
from crosscutting.condition_messages import print_info

import subprocess


def execute_command(command, *args):
    subprocess_command = [command]
    subprocess_command.extend(args)

    print_info(f'{strings.EXECUTING} {command} {" ".join(args)}')

    result = subprocess.run(subprocess_command, stdout=subprocess.PIPE)

    return result.stdout
