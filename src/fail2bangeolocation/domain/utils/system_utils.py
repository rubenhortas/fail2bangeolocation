import subprocess

from fail2bangeolocation.crosscutting import strings
from fail2bangeolocation.crosscutting.condition_messages import print_info, print_exception


def execute_command(command: str, *args) -> bytes | None:
    try:
        subprocess_command = [command]
        subprocess_command.extend(args)

        print_info(f"{strings.EXECUTING} {command} {' '.join(args)}")
        result = subprocess.run(subprocess_command, stdout=subprocess.PIPE)

        return result.stdout
    except Exception as e:
        print_exception(e)

        return None
