import unittest

from src.fail2bangeolocation.infrastructure.reallyfreegeoip import get_location


# noinspection SpellCheckingInspection
class Reallyfreegeoip(unittest.TestCase):
    def test_get_location(self):
        ip = '207.188.187.163'
        expected_country = 'United States'
        expected_city = ''

        country, city = get_location(ip)
        self.assertTupleEqual((expected_country, expected_city), (country, city))


if __name__ == '__main__':
    unittest.main()  # run all tests
