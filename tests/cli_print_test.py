import unittest

from src.fail2bangeolocation.domain.country import Country
from src.fail2bangeolocation.presentation.cli_print import print_locations, print_unlocated_ips


# noinspection PyMethodMayBeStatic
class CliPrintTest(unittest.TestCase):
    def setUp(self):
        self.locations = [Country('United Kingdom', {'London': 3}, False),
                          Country('Japan', {'Unknown': 2, 'Osaka': 1}, False),
                          Country('France', {'Reims': 1, 'Unknown': 1}, False),
                          Country('United States', {'Los Angeles': 1}, False),
                          Country('China', {'Unknown': 1}, False),
                          Country('Australia', {'Unknown': 1}, False)]

        self.unlocated_ips = ['0.0.0.0', '1.1.1.1', '2.2.2.2']

    def test_print_locations(self):
        print_locations(self.locations, False)
        print()
        print_locations(self.locations, True)

    def test_print_not_located(self):
        print_unlocated_ips(self.unlocated_ips)


if __name__ == '__main__':
    unittest.main()  # run all tests
