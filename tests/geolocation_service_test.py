import unittest

from application import geolocation, fail2ban
from crosscutting import strings
from domain.Location import Location


class GeoLocationServiceTests(unittest.TestCase):
    def setUp(self):
        self.locations = []

        location = Location('Spain', 'Lugo')
        self.locations.append(location)
        self.locations.append(location)

        location = Location('Spain', 'A Coruña')
        self.locations.append(location)

        location = Location('Spain', None)
        self.locations.append(location)

        location = Location('Portugal', 'Lisbon')
        self.locations.append(location)

        location = Location('USA', 'New York')
        self.locations.append(location)

        location = Location('Japan', 'Yokohama')
        self.locations.append(location)

        location = Location('Japan', 'Tokyo')
        self.locations.append(location)

        location = Location('France', None)
        self.locations.append(location)
        self.locations.append(location)

        self.expected_attempts = {'Spain': {'Lugo': 2, 'A Coruña': 1, None: 1}, 'Portugal': {'Lisbon': 1},
                                  'USA': {'New York': 1}, 'Japan': {'Yokohama': 1, 'Tokyo': 1}, 'France': {None: 2}}

        self.expected_result_sorted_by_country = {'Spain': 4, 'France': 2, 'Japan': 2, 'Portugal': 1, 'USA': 1}
        self.expected_result_sorted_by_city = {'Spain': {'Lugo': 2, 'A Coruña': 1, strings.UNKNOWN: 1},
                                               'France': {strings.UNKNOWN: 2}, 'Japan': {'Tokyo': 1, 'Yokohama': 1},
                                               'Portugal': {'Lisbon': 1}, 'USA': {'New York': 1}}

        self.ips_not_geolocated = ['1.2.3.4', '4.5.6.7', '10.11.12.13.14']

        self.fail2ban_banned_ips = [{'sshd': ['1.1.1.1', '1.1.1.2', '1.1.1.3']},
                                    {'other': ['2.2.2.1', '2.2.2.2', '2.2.2.3']}]
        self.expected_result_fail2ban_banned_ips = ['1.1.1.1', '1.1.1.2', '1.1.1.3', '2.2.2.1', '2.2.2.2', '2.2.2.3']

        self.fail2ban_server_banned_ips = b'Status for the jail: sshd\n|- Filter\n|  |- Currently failed:\t0\n|  |- Total failed:\t2102\n|  `- File list:\t/var/log/auth.log\n`- Actions\n   |- Currently banned:\t2773\n   |- Total banned:\t2857\n   `- Banned IP list:\t1.1.1.1 1.1.1.2 2.2.2.1 2.2.2.2 2.2.2.3\n'
        self.expected_result_fail2ban_server_banned_ips = ['1.1.1.1', '1.1.1.2', '2.2.2.1', '2.2.2.2', '2.2.2.3']

    def test_get_attempts(self):
        attempts = geolocation._get_attempts(self.locations)
        self.assertDictEqual(self.expected_attempts, attempts)

    def test_sort_by_country(self):
        result = geolocation._sort(self.expected_attempts, False)
        self.assertDictEqual(self.expected_result_sorted_by_country, result)

    def test_sort_by_city(self):
        result = geolocation._sort(self.expected_attempts, True)
        self.assertDictEqual(self.expected_result_sorted_by_city, result)

    def test_print_stats_by_country(self):
        print('Sorted by country')
        geolocation._print_attempts(self.expected_result_sorted_by_country, False)
        print()

    def test_print_stats_by_city(self):
        print('Sorted by country and city')
        geolocation._print_attempts(self.expected_result_sorted_by_city, True)

    def test_print_not_geolocated(self):
        geolocation._print_not_found(self.ips_not_geolocated)

    def test_parse_banned_ips(self):
        result = fail2ban._parse_banned_ips(self.fail2ban_banned_ips)
        self.assertListEqual(self.expected_result_fail2ban_banned_ips, result)

    def test_parse_server_banned_ips(self):
        result = fail2ban._parse_server_banned_ips(self.fail2ban_server_banned_ips)
        self.assertListEqual(self.expected_result_fail2ban_server_banned_ips, result)


if __name__ == '__main__':
    unittest.main()  # run all tests
