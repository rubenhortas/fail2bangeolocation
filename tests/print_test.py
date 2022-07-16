import unittest

from fail2bangeolocation.application import geolocation
from fail2bangeolocation.crosscutting import strings


class PrintTest(unittest.TestCase):
    def setUp(self):
        self.attempts_sorted_by_country = {'Spain': 4, 'France': 2, 'Japan': 2, 'Portugal': 1, 'USA': 1}

        self.attempts_sorted_by_country_and_city = {'Spain': {'Lugo': 2, 'A Coruña': 1, strings.UNKNOWN: 1},
                                                    'France': {strings.UNKNOWN: 2},
                                                    'Japan': {'Tokyo': 1, 'Yokohama': 1},
                                                    'Portugal': {'Lisbon': 1}, 'USA': {'New York': 1}}

        self.ips_not_geolocated = ['1.2.3.4', '4.5.6.7', '10.11.12.13.14']

    def test_print_sorted_by_country(self):
        print('Sorted by country')
        geolocation._print_attempts(self.attempts_sorted_by_country, None)
        print()

    def test_print_sorted_by_country_and_city(self):
        print('Sorted by country and city')
        geolocation._print_attempts(self.attempts_sorted_by_country, self.attempts_sorted_by_country_and_city)
        print()

    def test_print_not_geolocated(self):
        print('Ips not geolocated')
        geolocation._print_not_found(self.ips_not_geolocated)
        print()


if __name__ == '__main__':
    unittest.main()  # run all tests
