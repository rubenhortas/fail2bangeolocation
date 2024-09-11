import unittest

from src.fail2bangeolocation.domain.country import Country
# noinspection PyProtectedMember
from src.fail2bangeolocation.application.location import _group_locations, _sort_grouped_locations


# noinspection SpellCheckingInspection
class LocationTest(unittest.TestCase):
    def setUp(self):
        self.returned_locations = [('United States', 'Los Angeles'), ('Australia', ''), ('Japan', ''), ('China', ''),
                                   ('United Kingdom', 'London'), ('United Kingdom', 'London'), ('France', ''),
                                   ('Japan', 'Osaka'), ('France', 'Reims'), ('United Kingdom', 'London'), ('Japan', '')]
        self.expected_grouped_locations = {'Australia': {'Unknown': 1}, 'China': {'Unknown': 1}, 'France': {'Reims': 1, 'Unknown': 1}, 'Japan': {'Osaka': 1, 'Unknown': 2}, 'United Kingdom': {'London': 3}, 'United States': {'Los Angeles': 1}}
        self.expected_sorted_locations_by_country = [Country('United Kingdom', {'London': 3}, False), Country('Japan', {'Osaka': 1, 'Unknown': 2}, False), Country('France', {'Reims': 1, 'Unknown': 1}, False), Country('United States', {'Los Angeles': 1}, False), Country('China', {'Unknown': 1}, False), Country('Australia', {'Unknown': 1}, False)]
        self.unsorted_locations = {'United Kingdom': {'London': 3}, 'France': {'Reims': 1, 'Unknown': 1}, 'China': {'Unknown': 1}, 'United States': {'Los Angeles': 1}, 'Japan': {'Osaka': 1, 'Unknown': 2}, 'Australia': {'Unknown': 1}}
        # show_cities = False to avoid sorting the cities when creating the Country object
        self.expected_sorted_locations_by_country_and_city = [Country('United Kingdom', {'London': 3}, False), Country('Japan', {'Unknown': 2, 'Osaka': 1}, False), Country('France', {'Reims': 1, 'Unknown': 1}, False), Country('United States', {'Los Angeles': 1}, False), Country('China', {'Unknown': 1}, False), Country('Australia', {'Unknown': 1}, False)]

    def test_group_locations(self):
        self.assertDictEqual(self.expected_grouped_locations, _group_locations(self.returned_locations))

    def test_sort_grouped_locations_by_country(self):
        self.assertListEqual(self.expected_sorted_locations_by_country,
                             _sort_grouped_locations(self.unsorted_locations, False))

    def test_sort_grouped_locations_by_country_and_city(self):
        sorted_locations = _sort_grouped_locations(self.unsorted_locations, True)

        for expected_result, result in zip(self.expected_sorted_locations_by_country_and_city, sorted_locations):
            self.assertEqual(expected_result, result)
            self.assertEqual(list(expected_result.cities), list(result.cities))


if __name__ == '__main__':
    unittest.main()  # run all tests
