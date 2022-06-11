import unittest

from application import geolocation_service
from domain.Location import Location


class GeoLocationServiceTests(unittest.TestCase):
    def test_get_stats(self):
        locations = []

        location = Location("Spain", "Lugo")
        locations.append(location)

        location = Location("Spain", "A Coruña")
        locations.append(location)

        location = Location("Spain", "Lugo")
        locations.append(location)

        location = Location("Portugal", "Lisbon")
        locations.append(location)

        location = Location("USA", "New York")
        locations.append(location)

        location = Location("Japan", "Tokyo")
        locations.append(location)

        location = Location("France", None)
        locations.append(location)

        location = Location("France", None)
        locations.append(location)

        expected_stats = {'Spain': {'Lugo': 2, 'A Coruña': 1}, 'Portugal': {'Lisbon': 1}, 'USA': {'New York': 1},
                          'Japan': {'Tokyo': 1}, 'France': {None: 2}}
        stats = geolocation_service.get_stats(locations)

        self.assertDictEqual(expected_stats, stats)


if __name__ == "__main__":
    unittest.main()  # run all tests
