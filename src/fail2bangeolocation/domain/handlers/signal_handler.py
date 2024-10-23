from types import FrameType

from crosscutting import condition_messages, strings


# noinspection PyUnusedLocal
def handle_sigint(signal: int, frame: FrameType) -> None:
    condition_messages.print_info(strings.STOPPED)
    exit(0)
