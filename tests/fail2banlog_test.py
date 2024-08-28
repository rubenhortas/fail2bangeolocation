import unittest

from src.fail2bangeolocation.application.fail2banlog import get_banned_ips


class Fail2banLogTest(unittest.TestCase):
    def setUp(self):
        # noinspection SpellCheckingInspection
        self.log_file = r'/home/rubenhortas/fail2bangeolocation/tests/fail2ban.log'

    def test_get_banned_ips(self):
        get_banned_ips(self.log_file, True)


if __name__ == '__main__':
    unittest.main()  # run all tests
