from colorama import Fore, Style

from fail2bangeolocation.crosscutting import strings


class Tag:
    error = f"[{Style.BRIGHT}{Fore.RED}{strings.ERROR}{Style.RESET_ALL}]"
    exception = f"[{Style.BRIGHT}{Fore.RED}{strings.EXCEPTION}{Style.RESET_ALL}]"
    info = f"[{Style.BRIGHT}{Fore.GREEN}*{Style.RESET_ALL}]"
