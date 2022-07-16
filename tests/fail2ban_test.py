import unittest

from fail2bangeolocation.application import fail2ban


class Fail2banServiceTest(unittest.TestCase):
    def setUp(self):
        self.fail2ban_banned_ips = b"[{'sshd': ['1.1.1.1', '1.1.1.2', '1.1.1.3']}, {'other': ['2.2.2.1', '2.2.2.2', '2.2.2.3']}]\n"
        self.expected_result_fail2ban_banned_ips = ['1.1.1.1', '1.1.1.2', '1.1.1.3', '2.2.2.1', '2.2.2.2', '2.2.2.3']

        self.fail2ban_server_banned_ips = b'Status for the jail: sshd\n|- Filter\n|  |- Currently failed:\t0\n|  |- Total failed:\t2102\n|  `- File list:\t/var/log/auth.log\n`- Actions\n   |- Currently banned:\t2773\n   |- Total banned:\t2857\n   `- Banned IP list:\t1.1.1.1 1.1.1.2 2.2.2.1 2.2.2.2 2.2.2.3\n'
        self.expected_result_fail2ban_server_banned_ips = ['1.1.1.1', '1.1.1.2', '2.2.2.1', '2.2.2.2', '2.2.2.3']

    def test_parse_banned_ips(self):
        result = fail2ban._parse_banned_ips(self.fail2ban_banned_ips)
        self.assertListEqual(self.expected_result_fail2ban_banned_ips, result)

    def test_parse_server_banned_ips(self):
        result = fail2ban._parse_server_banned_ips(self.fail2ban_server_banned_ips)
        self.assertListEqual(self.expected_result_fail2ban_server_banned_ips, result)


if __name__ == '__main__':
    unittest.main()  # run all tests
