from presentation.color import Color


def print_country(country, counter=None):
    if not counter:
        print(f"{Color.bold_green}{country}{Color.end}")
    else:
        print(f"{Color.bold_green}{country}{Color.end}: {counter}")


def print_city(city, counter=None):
    if not counter:
        print(f"\t{Color.bold_yellow}{city}{Color.end}")
    else:
        print(f"\t{Color.bold_yellow}{city}{Color.end}: {counter}")
