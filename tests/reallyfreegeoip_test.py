import unittest

from src.fail2bangeolocation.application.reallyfreegeoip import get_location


# noinspection SpellCheckingInspection
class Reallyfreegeoip(unittest.TestCase):
    def setUp(self):
        self.ip = '207.188.187.163'
        self.expected_country = 'United States'
        self.expected_city = ''

    def test_get_location(self):
        country, city = get_location(self.ip)
        self.assertTupleEqual((self.expected_country, self.expected_city), (country, city))


if __name__ == '__main__':
    unittest.main()  # run all tests
