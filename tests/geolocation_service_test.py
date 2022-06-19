import unittest

from application import geolocation
from crosscutting import strings
from domain.Location import Location


class GeoLocationServiceTests(unittest.TestCase):
    def setUp(self):
        self.locations = []

        location = Location('Spain', 'Lugo')
        self.locations.append(location)

        location = Location('Spain', 'A Coruña')
        self.locations.append(location)

        location = Location('Spain', 'Lugo')
        self.locations.append(location)

        location = Location('Portugal', 'Lisbon')
        self.locations.append(location)

        location = Location('USA', 'New York')
        self.locations.append(location)

        location = Location('Japan', 'Yokohama')
        self.locations.append(location)

        location = Location('Japan', 'Tokyo')
        self.locations.append(location)

        location = Location('France', None)
        self.locations.append(location)

        location = Location('France', None)
        self.locations.append(location)

        self.expected_attempts = {'Spain': {'Lugo': 2, 'A Coruña': 1}, 'Portugal': {'Lisbon': 1},
                                  'USA': {'New York': 1}, 'Japan': {'Tokyo': 1, 'Yokohama': 1}, 'France': {None: 2}}

        self.expected_result_sorted_by_country = {'Spain': 3, 'France': 2, 'Japan': 2, 'Portugal': 1, 'USA': 1}

        self.expected_result_sorted_by_city = {'Spain': {'Lugo': 2, 'A Coruña': 1}, 'France': {strings.UNKNOWN: 2},
                                               'Japan': {'Tokyo': 1, 'Yokohama': 1}, 'Portugal': {'Lisbon': 1},
                                               'USA': {'New York': 1}}

        self.ips_not_geolocated = ['1.2.3.4', '4.5.6.7', '10.11.12.13.14']

    def test_get_attempts(self):
        attempts = geolocation._get_attempts(self.locations)
        self.assertDictEqual(self.expected_attempts, attempts)

    def test_sort(self):
        result = geolocation._sort(self.expected_attempts, False)
        self.assertDictEqual(self.expected_result_sorted_by_country, result)

    def test_print_stats_grouped_by_city(self):
        result = geolocation._sort(self.expected_attempts, True)
        self.assertDictEqual(self.expected_result_sorted_by_city, result)

    def test_print_stats(self):
        print('Sorted by country')
        geolocation._print_attempts(self.expected_result_sorted_by_country, False)

        print()

        print('Sorted by country and city')
        geolocation._print_attempts(self.expected_result_sorted_by_city, True)

    def test_print_not_geolocated(self):
        geolocation._print_not_found(self.ips_not_geolocated)


if __name__ == '__main__':
    unittest.main()  # run all tests
