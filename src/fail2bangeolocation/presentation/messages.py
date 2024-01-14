from colorama import Fore, Style


def print_country(country, counter=None):
    if not counter:
        print(f"{Style.BRIGHT}{Fore.GREEN}{country}{Style.RESET_ALL}")
    else:
        print(f"{Style.BRIGHT}{Fore.GREEN}{country}{Style.RESET_ALL}: {counter}")


def print_city(city, counter):
    print(f"\t{Style.BRIGHT}{Fore.YELLOW}{city}{Style.RESET_ALL}: {counter}")


def print_error(msg):
    print(f"{Style.BRIGHT}{Fore.RED}(!){Style.RESET_ALL} {msg}")
