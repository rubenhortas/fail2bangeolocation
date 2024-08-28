import unittest

from src.fail2bangeolocation.application import geolocation
from src.fail2bangeolocation.crosscutting import strings


class GeoLocationTest(unittest.TestCase):
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

        self.grouped_locations = {'Spain': {'Lugo': 2, 'A Coruña': 1, strings.UNKNOWN: 1}, 'Portugal': {'Lisbon': 1},
                                  'USA': {'New York': 1}, 'Japan': {'Yokohama': 1, 'Tokyo': 1},
                                  'France': {strings.UNKNOWN: 2}}

        self.grouped_locations_sorted_by_country_dict = {'Spain': 4, 'France': 2, 'Japan': 2, 'Portugal': 1, 'USA': 1}

        self.grouped_locations_sorted_by_country = (self.grouped_locations_sorted_by_country_dict, None)

        self.grouped_locations_sorted_by_country_and_city = {'Spain': {'Lugo': 2, 'A Coruña': 1, strings.UNKNOWN: 1},
                                                             'France': {strings.UNKNOWN: 2},
                                                             'Japan': {'Tokyo': 1, 'Yokohama': 1},
                                                             'Portugal': {'Lisbon': 1}, 'USA': {'New York': 1}}

        self.ips_not_located = ['1.2.3.4', '4.5.6.7', '10.11.12.13.14']

    def test_group_locations(self):
        grouped_locations = geolocation._group_locations(self.renamed_locations)
        self.assertEqual(self.grouped_locations, grouped_locations)

    def test_sort_by_country(self):
        grouped_locations_sorted_by_country = geolocation._sort(self.grouped_locations, False)
        self.assertTupleEqual(self.grouped_locations_sorted_by_country, grouped_locations_sorted_by_country)

    def test_sort_by_city(self):
        grouped_locations_sorted_by_country, grouped_locations_sorted_by_country_and_city = geolocation._sort(
            self.grouped_locations,
            True)
        self.assertDictEqual(self.grouped_locations_sorted_by_country_dict, grouped_locations_sorted_by_country)
        self.assertDictEqual(self.grouped_locations_sorted_by_country_and_city,
                             grouped_locations_sorted_by_country_and_city)


if __name__ == '__main__':
    unittest.main()  # run all tests
