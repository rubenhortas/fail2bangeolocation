import unittest

from fail2bangeolocation.application.reallyfreegeoip import get_location


# noinspection SpellCheckingInspection
class Reallyfreegeoip(unittest.TestCase):
    def setUp(self):
        self.ip = '207.188.187.163'
        self.result = {"ip": "207.188.187.163", "country_code": "US", "country_name": "United States",
                       "region_code": "", "region_name": "", "city": "", "zip_code": "", "time_zone": "America/Chicago",
                       "latitude": 37.751, "longitude": -97.822, "metro_code": 0}

    def test_get_location(self):
        country, city = get_location(self.ip)
        self.assertTupleEqual(('United States', ''), (country, city))


if __name__ == '__main__':
    unittest.main()  # run all tests
