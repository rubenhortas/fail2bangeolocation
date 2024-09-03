import unittest


# noinspection SpellCheckingInspection
class GeolocationTest(unittest.TestCase):
    def setUp(self):
        self.locations = {'United Kingdom': ['London', 'London', 'London'],
                          'Japan': ['Unknown', 'Osaka', 'Unknown'],
                          'France': ['Unknown', 'Reims'],
                          'China': ['Unknown'],
                          'United States': ['Los Angeles'],
                          'Australia': ['Unknown']}
        self.ips_not_located = ['0.0.0.1', '0.0.0.0']

    def test_group_locations(self):
        return True


if __name__ == '__main__':
    unittest.main()  # run all tests
