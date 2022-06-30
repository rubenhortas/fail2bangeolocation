import unittest

from application import geolocation
from crosscutting import strings


class GeoLocationServiceTests(unittest.TestCase):
    def setUp(self):
        self.locations = []

        location = ('Spain', 'Lugo')
        self.locations.append(location)
        self.locations.append(location)

        location = ('Spain', 'A Coruña')
        self.locations.append(location)

        location = ('Spain', None)
        self.locations.append(location)

        location = ('Portugal', 'Lisbon')
        self.locations.append(location)

        location = ('USA', 'New York')
        self.locations.append(location)

        location = ('Japan', 'Yokohama')
        self.locations.append(location)

        location = ('Japan', 'Tokyo')
        self.locations.append(location)

        location = ('France', None)
        self.locations.append(location)
        self.locations.append(location)

        self.renamed_locations = [('Spain', 'Lugo'), ('Spain', 'Lugo'), ('Spain', 'A Coruña'),
                                  ('Spain', strings.UNKNOWN), ('Portugal', 'Lisbon'), ('USA', 'New York'),
                                  ('Japan', 'Yokohama'), ('Japan', 'Tokyo'), ('France', strings.UNKNOWN),
                                  ('France', strings.UNKNOWN)]

        self.failed_attempts = {'Spain': {'Lugo': 2, 'A Coruña': 1, strings.UNKNOWN: 1}, 'Portugal': {'Lisbon': 1},
                                'USA': {'New York': 1}, 'Japan': {'Yokohama': 1, 'Tokyo': 1},
                                'France': {strings.UNKNOWN: 2}}

        self.expected_result_sorted_by_country = {'Spain': 4, 'France': 2, 'Japan': 2, 'Portugal': 1, 'USA': 1}
        self.expected_result_sorted_by_city = {'Spain': {'Lugo': 2, 'A Coruña': 1, strings.UNKNOWN: 1},
                                               'France': {strings.UNKNOWN: 2}, 'Japan': {'Tokyo': 1, 'Yokohama': 1},
                                               'Portugal': {'Lisbon': 1}, 'USA': {'New York': 1}}

        self.ips_not_geolocated = ['1.2.3.4', '4.5.6.7', '10.11.12.13.14']

    def test_rename_locations(self):
        renamed_locations = geolocation._rename_unknown_locations(self.locations)
        self.assertListEqual(self.renamed_locations, renamed_locations)

    def test_get_failed_attempts(self):
        failed_attempts = geolocation._get_failed_attempts(self.renamed_locations)
        self.assertEqual(self.failed_attempts, failed_attempts)

    def test_sort_by_country(self):
        result = geolocation._sort(self.failed_attempts, False)
        self.assertDictEqual(self.expected_result_sorted_by_country, result)

    # def test_sort_by_city(self):
    #     result = geolocation._sort(self.failed_attempts, True)
    #     self.assertDictEqual(self.expected_result_sorted_by_city, result)


if __name__ == '__main__':
    unittest.main()  # run all tests
