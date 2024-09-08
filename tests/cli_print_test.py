import unittest

from src.fail2bangeolocation.application.country import Country
from src.fail2bangeolocation.presentation.cli_print import print_locations, print_not_located


# noinspection PyMethodMayBeStatic
class CliPrintTest(unittest.TestCase):
    def test_print_locations(self):
        locations = [Country('United Kingdom', {'London': 3}, False),
                     Country('Japan', {'Unknown': 2, 'Osaka': 1}, False),
                     Country('France', {'Reims': 1, 'Unknown': 1}, False),
                     Country('United States', {'Los Angeles': 1}, False),
                     Country('China', {'Unknown': 1}, False),
                     Country('Australia', {'Unknown': 1}, False)]

        print_locations(locations, False)
        print()
        print_locations(locations, True)

    def test_print_not_located(self):
        ips = ['0.0.0.0', '1.1.1.1', '2.2.2.2']
        print_not_located(ips)


if __name__ == '__main__':
    unittest.main()  # run all tests
