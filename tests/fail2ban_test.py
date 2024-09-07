import unittest
from unittest.mock import patch

from src.fail2bangeolocation.application.fail2ban import get_banned_ips


# noinspection SpellCheckingInspection
class Fail2banTest(unittest.TestCase):
    @patch('src.fail2bangeolocation.application.fail2ban.execute_command')
    def test_server_none(self, mock_execute_command):
        mock_execute_command.return_value = None
        self.assertEqual([], get_banned_ips())

    @patch('src.fail2bangeolocation.application.fail2ban.execute_command')
    def test_command_returns_none(self, mock_execute_command):
        fail2ban_banned = b"[{'sshd': ['1.1.1.1', '1.1.1.2', '1.1.1.3']}, {'http': ['2.2.2.1', '2.2.2.2', '2.2.2.3']}]\n"
        fail2ban_banned_expected_result = ['1.1.1.1', '1.1.1.2', '1.1.1.3', '2.2.2.1', '2.2.2.2', '2.2.2.3']

        mock_execute_command.return_value = fail2ban_banned
        self.assertEqual(fail2ban_banned_expected_result, get_banned_ips())

    @patch('src.fail2bangeolocation.application.fail2ban.execute_command')
    def test_server_sshd(self, mock_execute_command):
        fail2ban_status_sshd = b'''Status for the jail: sshd
                                        |- Filter
                                        |  |- Currently failed: 0
                                        |  |- Total failed:     1
                                        |  `- File list:        /var/log/auth.log
                                        `- Actions
                                            |- Currently banned: 1
                                            |- Total banned:     1
                                            `- Banned IP list:   5.181.86.251'''
        fail2ban_status_sshd_expected_result = ['5.181.86.251']

        mock_execute_command.return_value = fail2ban_status_sshd
        self.assertEqual(fail2ban_status_sshd_expected_result, get_banned_ips('sshd'))


if __name__ == '__main__':
    unittest.main()  # run all tests
