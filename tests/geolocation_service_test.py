import unittest

from application import geolocation_service
from domain.Location import Location


class GeoLocationServiceTests(unittest.TestCase):
    def setUp(self):
        """Call before every test case."""
        self.locations = []

        location = Location("Spain", "Lugo")
        self.locations.append(location)

        location = Location("Spain", "A Coruña")
        self.locations.append(location)

        location = Location("Spain", "Lugo")
        self.locations.append(location)

        location = Location("Portugal", "Lisbon")
        self.locations.append(location)

        location = Location("USA", "New York")
        self.locations.append(location)

        location = Location("Japan", "Tokyo")
        self.locations.append(location)

        location = Location("France", None)
        self.locations.append(location)

        location = Location("France", None)
        self.locations.append(location)

        self.expected_stats = {'Spain': {'Lugo': 2, 'A Coruña': 1}, 'Portugal': {'Lisbon': 1}, 'USA': {'New York': 1},
                               'Japan': {'Tokyo': 1}, 'France': {None: 2}}

    def test_get_stats(self):
        stats = geolocation_service.get_stats(self.locations)

        self.assertDictEqual(self.expected_stats, stats)

    def test_sort(self):
        result = geolocation_service.sort(self.expected_stats, False)
        expected_result = {'Spain': 3, 'France': 2, 'Portugal': 1, 'USA': 1, 'Japan': 1}

        self.assertDictEqual(result, expected_result)

    def test_print_stats_grouped_by_city(self):
        result = geolocation_service.sort(self.expected_stats, True)
        expected_result = {'Spain': {'Lugo': 2, 'A Coruña': 1}, 'France': {None: 2}, 'Portugal': {'Lisbon': 1},
                           'USA': {'New York': 1}, 'Japan': {'Tokyo': 1}}

        self.assertDictEqual(result, expected_result)

    def test_print_stats(self):
        result = {'Spain': 3, 'France': 2, 'Portugal': 1, 'USA': 1, 'Japan': 1}
        result_by_city = {'Spain': {'Lugo': 2, 'A Coruña': 1}, 'France': {None: 2}, 'Portugal': {'Lisbon': 1},
                          'USA': {'New York': 1}, 'Japan': {'Tokyo': 1}}

        geolocation_service.print_stats(result, False)
        geolocation_service.print_stats(result_by_city, True)


if __name__ == "__main__":
    unittest.main()  # run all tests
