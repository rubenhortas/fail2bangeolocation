import unittest

from fail2bangeolocation.application.geolocation import _group_locations, _sort_grouped_locations


# noinspection SpellCheckingInspection
class GeolocationTest(unittest.TestCase):
    def setUp(self):
        self.ips = ['68.168.142.91', '1.1.1.1', '0.0.0.0', '43.155.113.19', '120.92.111.55', '178.62.111.142',
                    '138.68.131.49', '2.2.2.2', '8.38.172.54', '163.172.87.64', '167.99.89.94', '0.0.0.1',
                    '43.156.124.114']
        self.returned_locations = [('United States', 'Los Angeles'), ('Australia', ''), ('Japan', ''), ('China', ''),
                                   ('United Kingdom', 'London'), ('United Kingdom', 'London'), ('France', ''),
                                   ('Japan', 'Osaka'), ('France', 'Reims'), ('United Kingdom', 'London'), ('Japan', '')]
        self.expected_grouped_locations = {'Australia': {'Unknown': 1}, 'China': {'Unknown': 1},
                                           'France': {'Reims': 1, 'Unknown': 1}, 'Japan': {'Osaka': 1, 'Unknown': 2},
                                           'United Kingdom': {'London': 3}, 'United States': {'Los Angeles': 1}}
        self.unsorted_locations = {'United Kingdom': {'London': 3}, 'France': {'Reims': 1, 'Unknown': 1},
                                   'China': {'Unknown': 1}, 'United States': {'Los Angeles': 1},
                                   'Japan': {'Osaka': 1, 'Unknown': 2}, 'Australia': {'Unknown': 1}}
        self.sorted_locations = {'Australia': {'Unknown': 1}, 'China': {'Unknown': 1},
                                 'France': {'Reims': 1, 'Unknown': 1}, 'Japan': {'Unknown': 2, 'Osaka': 1},
                                 'United Kingdom': {'London': 3}, 'United States': {'Los Angeles': 1}}

    def test_group_locations(self):
        self.assertDictEqual(self.expected_grouped_locations, _group_locations(self.returned_locations))

    def test_sort_grouped_locations(self):
        try:
            _sort_grouped_locations(self.unsorted_locations)
        except Exception as e:
            msg = e


if __name__ == '__main__':
    unittest.main()  # run all tests
