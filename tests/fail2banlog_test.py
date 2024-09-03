import os
import unittest

from src.fail2bangeolocation.application.fail2banlog import get_banned_ips


class Fail2banLogTest(unittest.TestCase):
    def setUp(self):
        current_dir = os.getcwd()
        absolute_test_logs_path = os.path.join(current_dir, 'logs')

        self.empty_log = os.path.join(absolute_test_logs_path, 'empty.log')
        self.mini_log = os.path.join(absolute_test_logs_path, 'fail2ban_mini.log')
        self.log = os.path.join(absolute_test_logs_path, 'fail2ban.log')

        self.mini_log_add_unbanned_expected_result = ['68.168.142.91', '1.1.1.1', '0.0.0.0', '43.155.113.19',
                                                      '120.92.111.55', '178.62.111.142', '138.68.131.49', '2.2.2.2',
                                                      '8.38.172.54', '163.172.87.64', '167.99.89.94', '0.0.0.1',
                                                      '43.156.124.114']
        self.mini_log_expected_result = ['120.92.111.55', '43.156.124.114', '167.99.89.94', '43.155.113.19',
                                         '68.168.142.91', '178.62.111.142', '8.38.172.54', '138.68.131.49',
                                         '163.172.87.64']

        self.log_add_unbanned_expected_result = ['8.210.155.49', '134.209.175.24', '103.139.42.55', '189.29.171.10',
                                                 '147.182.188.81', '3.138.36.133', '143.244.190.237', '43.154.38.204',
                                                 '217.92.15.51', '35.185.183.125', '106.241.33.158', '68.168.142.91',
                                                 '43.154.192.142', '196.43.103.254', '23.105.219.71', '154.221.26.62',
                                                 '200.160.111.44', '43.154.158.237', '144.126.197.136',
                                                 '213.168.248.63',
                                                 '95.85.34.53', '144.22.248.23', '111.67.197.223', '114.33.239.231',
                                                 '43.154.42.83', '200.29.111.20', '106.75.10.4', '87.237.233.14',
                                                 '203.240.232.56', '154.94.4.209', '43.154.193.125', '123.120.11.143',
                                                 '134.17.16.92', '43.154.89.83', '52.163.119.141', '202.125.94.212',
                                                 '103.233.0.121', '124.121.30.231', '218.75.156.247', '123.138.161.69',
                                                 '43.204.32.184', '43.156.123.191', '41.160.238.202', '43.156.124.37',
                                                 '43.156.127.187', '104.248.123.197', '43.132.156.23', '186.209.41.35',
                                                 '58.20.54.143', '43.134.106.247', '178.62.243.101', '128.199.19.74',
                                                 '161.35.24.244', '123.100.226.242', '178.62.81.147', '137.184.54.207',
                                                 '170.106.113.73', '122.160.51.88', '167.235.54.246', '104.248.91.215',
                                                 '180.76.163.135', '129.226.15.250', '95.85.23.145', '51.222.205.124',
                                                 '213.215.163.233', '43.156.125.110', '35.227.57.104', '103.140.18.90',
                                                 '43.155.82.137', '75.119.145.61', '150.136.65.184', '189.206.165.62',
                                                 '43.134.29.226', '139.162.232.35', '210.195.0.59', '114.67.234.182',
                                                 '167.172.158.195', '120.48.47.43', '52.183.141.32', '43.128.18.253',
                                                 '13.76.164.123', '188.166.113.144', '150.185.5.105', '128.134.30.40',
                                                 '102.164.61.62', '43.154.192.161', '154.73.36.7', '106.249.241.58',
                                                 '159.223.150.43', '46.101.18.185', '202.67.9.54', '78.196.138.44',
                                                 '14.161.20.182', '182.72.142.62', '179.60.147.74', '20.123.235.249',
                                                 '185.217.127.171', '180.76.115.44', '37.139.16.229', '8.26.21.34',
                                                 '109.90.115.129', '46.101.135.232', '43.156.123.250', '152.32.193.111',
                                                 '218.245.63.192', '180.76.139.58', '43.156.125.234', '50.225.176.238',
                                                 '182.76.81.254', '43.156.128.57', '27.254.121.166', '72.167.34.2',
                                                 '43.154.67.173', '209.97.172.163', '43.154.63.36', '43.154.5.129',
                                                 '27.115.50.114', '206.189.55.226', '189.254.255.3', '177.103.187.233',
                                                 '61.82.54.57', '167.172.50.98', '62.210.207.22', '138.117.79.5',
                                                 '27.128.236.142', '178.62.111.142', '163.172.87.64', '43.129.244.207',
                                                 '43.154.202.94', '82.65.232.134', '101.231.146.36', '35.154.88.57',
                                                 '54.38.240.40', '162.243.146.147', '203.150.228.94', '192.210.207.67',
                                                 '104.248.58.66', '46.101.254.194', '201.124.26.152', '103.172.205.51',
                                                 '103.246.106.118', '220.243.178.124', '35.199.95.142',
                                                 '114.34.229.236',
                                                 '82.165.167.194', '201.86.177.110', '43.129.79.197', '175.140.139.145',
                                                 '61.93.240.18', '120.48.22.163', '144.24.129.100', '180.76.158.6',
                                                 '43.154.118.34', '157.230.98.148', '180.232.70.125', '69.49.245.238',
                                                 '128.199.230.181', '147.182.235.17', '157.230.42.195',
                                                 '85.236.173.182',
                                                 '20.115.75.130', '165.227.167.225', '128.199.225.7', '43.135.101.247',
                                                 '206.189.90.250', '43.154.70.239', '122.146.196.217', '202.81.116.199',
                                                 '159.223.12.197', '150.136.242.126', '128.199.68.220', '8.208.77.49',
                                                 '103.233.2.22', '43.154.43.6', '202.47.117.222', '128.199.26.132',
                                                 '128.199.115.255', '43.155.100.18', '43.154.233.68', '103.129.223.98',
                                                 '165.227.148.167', '180.76.51.65', '64.227.44.140', '90.84.195.216',
                                                 '43.156.124.68', '177.44.208.107', '69.10.39.91', '111.175.1.54',
                                                 '20.119.232.123', '159.65.138.77', '20.197.190.244', '179.1.85.121',
                                                 '13.79.122.130', '36.112.150.66', '118.70.233.231', '182.23.67.49',
                                                 '154.194.13.219', '211.43.12.240', '121.65.121.149', '102.130.114.226',
                                                 '41.63.9.36', '148.227.1.18', '43.155.90.59', '217.172.68.37',
                                                 '78.92.219.157', '51.75.224.152', '8.38.172.54', '77.50.183.22',
                                                 '157.245.40.222', '43.155.63.124', '20.226.46.159', '106.13.142.37',
                                                 '59.150.105.114', '68.183.136.217', '180.76.149.77', '8.215.45.162',
                                                 '31.22.108.179', '195.218.137.42', '143.198.171.44', '152.32.147.191',
                                                 '43.154.147.127', '180.76.138.143', '61.102.42.5', '178.62.215.237',
                                                 '191.239.116.211', '186.211.105.178', '171.217.67.69', '20.65.71.2',
                                                 '125.77.23.30', '43.154.174.101', '104.236.17.54', '134.209.8.231',
                                                 '134.122.8.241', '189.20.98.204', '43.156.123.97', '95.71.13.224',
                                                 '59.15.81.46', '165.227.124.168', '139.9.227.155', '182.23.63.22',
                                                 '128.199.143.246', '221.150.91.236', '41.77.186.96', '102.128.78.42',
                                                 '161.49.215.46', '209.141.35.242', '193.151.134.158', '43.132.248.159',
                                                 '36.153.118.90', '138.68.9.83', '165.232.35.74', '43.156.122.11',
                                                 '2.232.250.91', '120.224.163.253', '47.176.38.242', '188.165.189.244',
                                                 '220.180.112.208', '110.88.160.173', '159.65.159.164',
                                                 '93.188.166.219',
                                                 '101.43.146.238', '116.247.81.99', '31.220.58.225', '43.154.218.49',
                                                 '137.184.197.218', '103.133.57.242', '43.128.4.194', '110.185.85.117',
                                                 '83.0.66.35', '43.156.122.123', '5.58.8.4', '125.212.225.165',
                                                 '60.210.40.210', '94.179.133.22', '116.196.86.28', '178.20.41.108',
                                                 '106.12.185.16', '159.203.72.14', '177.115.54.135', '108.179.217.233',
                                                 '120.92.111.55', '209.14.71.31', '68.183.188.159', '43.154.157.102',
                                                 '43.154.168.239', '43.156.123.181', '64.225.25.59', '140.238.255.101',
                                                 '103.126.57.120', '43.154.50.6', '180.76.231.175', '43.154.202.193',
                                                 '95.217.80.125', '43.156.124.113', '139.198.169.252', '43.154.127.79',
                                                 '128.199.110.190', '41.79.78.41', '43.156.126.47', '190.128.171.250',
                                                 '103.102.42.42', '24.172.172.2', '192.241.236.30', '182.140.221.223',
                                                 '103.146.140.24', '222.124.177.148', '190.18.66.165',
                                                 '134.209.233.126', '208.113.201.147', '117.50.105.149',
                                                 '178.128.217.58', '221.140.57.201', '118.69.82.233', '159.65.111.89',
                                                 '222.124.214.10', '165.232.140.100', '111.160.100.50',
                                                 '200.118.57.190', '64.225.15.146', '170.254.229.211', '67.205.128.206',
                                                 '125.141.139.9', '43.154.188.69', '47.52.39.76', '122.11.148.34',
                                                 '106.13.85.194', '109.237.110.59', '128.116.154.5', '101.231.146.34',
                                                 '1.234.58.214', '5.141.81.226', '43.156.124.133', '43.154.36.254',
                                                 '203.101.126.19', '159.65.118.84', '103.134.89.240', '180.76.157.208',
                                                 '93.184.10.249', '186.225.150.215', '159.65.133.176', '43.154.42.99',
                                                 '43.154.69.93', '167.71.74.3', '164.160.40.182', '144.24.210.121',
                                                 '186.189.193.207', '211.44.198.209', '209.141.57.23', '43.133.44.86',
                                                 '161.35.127.144', '37.156.146.163', '43.132.156.117',
                                                 '121.183.132.151', '84.201.164.50', '203.162.79.29', '195.29.51.135',
                                                 '43.156.124.114', '157.245.75.41', '144.34.242.66', '68.183.80.221',
                                                 '182.254.140.176', '104.225.150.138', '43.154.129.76', '64.227.6.223',
                                                 '103.147.159.67', '43.134.31.33', '187.216.254.180', '202.134.18.102',
                                                 '45.90.108.26', '115.75.146.156', '139.59.27.36', '167.99.89.94',
                                                 '209.97.174.201', '156.232.6.68', '87.219.167.59', '188.166.1.95',
                                                 '184.96.190.11', '157.245.101.171', '103.95.12.143', '117.184.199.39',
                                                 '200.16.132.42', '23.95.80.57', '50.93.205.8', '159.65.97.125',
                                                 '193.233.185.220', '181.235.104.2', '62.113.108.169', '94.23.27.28',
                                                 '128.199.170.33', '81.70.50.89', '103.145.143.202', '43.155.113.19',
                                                 '138.68.131.49', '137.184.5.137', '124.123.66.20', '65.108.210.243',
                                                 '118.32.30.34', '139.59.80.151', '59.103.236.74', '43.156.78.159',
                                                 '164.92.226.99', '92.205.21.38', '23.224.39.151', '45.7.196.67',
                                                 '200.45.147.129', '103.144.245.66', '201.163.162.179',
                                                 '103.100.210.168', '62.201.207.53', '43.156.18.214', '147.139.31.249',
                                                 '43.156.125.191', '180.76.224.222', '147.182.195.174', '113.200.81.41',
                                                 '128.199.152.70', '183.88.192.172', '43.252.62.60', '111.67.199.217',
                                                 '120.48.2.61', '43.154.60.161', '14.232.243.151', '43.154.30.39',
                                                 '165.232.190.76', '190.196.70.21', '68.183.212.10', '43.156.124.180',
                                                 '188.234.247.110', '157.245.100.238', '178.18.252.186',
                                                 '43.156.124.167', '115.248.153.89', '162.243.73.244', '181.47.29.254',
                                                 '43.156.62.251', '200.7.198.66', '5.183.9.248', '43.156.125.41',
                                                 '43.154.47.14', '206.189.233.23', '147.182.141.153', '202.137.26.4',
                                                 '201.72.190.98', '138.201.109.89', '43.154.188.244', '171.244.139.237',
                                                 '43.156.123.128', '197.134.249.239', '165.227.50.84', '128.199.163.55',
                                                 '167.99.158.168', '43.156.123.106', '43.154.116.95', '159.65.127.239',
                                                 '185.74.5.184', '143.110.153.150', '211.210.152.106', '86.164.17.162',
                                                 '43.128.170.23', '219.142.247.146', '139.59.255.59', '160.251.7.202',
                                                 '43.154.17.118', '190.16.52.12', '43.134.1.59', '20.101.101.40',
                                                 '43.134.60.167', '210.114.18.28', '213.6.130.133', '43.129.211.157',
                                                 '167.99.137.141', '104.236.203.213', '41.59.82.183', '179.107.34.178',
                                                 '142.93.101.157']
        self.log_expected_result = ['43.156.124.180', '201.86.177.110', '43.156.124.114', '190.16.52.12',
                                    '165.227.148.167', '61.102.42.5', '180.76.231.175', '43.154.202.94',
                                    '46.101.135.232', '189.29.171.10', '138.68.9.83', '36.112.150.66',
                                    '211.210.152.106', '8.208.77.49', '143.198.171.44', '68.183.188.159',
                                    '104.236.203.213', '103.246.106.118', '161.49.215.46', '43.155.100.18',
                                    '164.160.40.182', '43.156.18.214', '43.132.248.159', '202.134.18.102',
                                    '43.155.82.137', '159.203.72.14', '122.11.148.34', '59.15.81.46', '43.134.31.33',
                                    '106.75.10.4', '161.35.127.144', '180.76.157.208', '43.129.79.197', '139.59.27.36',
                                    '147.182.235.17', '43.156.126.47', '72.167.34.2', '180.76.149.77', '43.132.156.23',
                                    '5.141.81.226', '144.126.197.136', '65.108.210.243', '128.199.68.220',
                                    '94.179.133.22', '177.103.187.233', '95.85.34.53', '170.254.229.211',
                                    '14.232.243.151', '180.76.115.44', '125.212.225.165', '46.101.18.185',
                                    '43.156.62.251', '147.139.31.249', '27.115.50.114', '201.163.162.179',
                                    '43.154.30.39', '161.35.24.244', '200.118.57.190', '142.93.101.157',
                                    '93.188.166.219', '167.172.158.195', '178.62.81.147', '52.163.119.141',
                                    '188.166.1.95', '69.10.39.91', '219.142.247.146', '43.154.70.239', '109.90.115.129',
                                    '43.135.101.247', '201.124.26.152', '209.97.174.201', '139.198.169.252',
                                    '43.154.192.142', '128.199.225.7', '157.230.98.148', '183.88.192.172',
                                    '50.93.205.8', '104.248.58.66', '206.189.55.226', '211.44.198.209', '52.183.141.32',
                                    '222.124.214.10', '124.123.66.20', '165.227.167.225', '43.154.168.239',
                                    '43.134.60.167', '180.76.163.135', '43.129.244.207', '200.160.111.44',
                                    '190.128.171.250', '203.162.79.29', '128.134.30.40', '138.117.79.5',
                                    '43.204.32.184', '106.249.241.58', '64.225.15.146', '180.76.139.58',
                                    '109.237.110.59', '58.20.54.143', '41.77.186.96', '110.88.160.173',
                                    '170.106.113.73', '43.156.124.37', '189.20.98.204', '8.210.155.49',
                                    '128.199.170.33', '165.232.35.74', '137.184.5.137', '140.238.255.101',
                                    '3.138.36.133', '103.100.210.168', '117.50.105.149', '43.156.124.113',
                                    '101.43.146.238', '180.76.51.65', '157.245.75.41', '117.184.199.39',
                                    '179.60.147.74', '159.65.111.89', '103.126.57.120', '8.38.172.54',
                                    '222.124.177.148', '189.206.165.62', '195.218.137.42', '43.154.38.204',
                                    '123.138.161.69', '27.128.236.142', '85.236.173.182', '147.182.195.174',
                                    '167.71.74.3', '13.76.164.123', '189.254.255.3', '43.156.78.159', '103.134.89.240',
                                    '111.67.197.223', '103.95.12.143', '188.165.189.244', '43.154.42.99',
                                    '154.221.26.62', '203.150.228.94', '122.146.196.217', '180.76.224.222',
                                    '45.90.108.26', '210.195.0.59', '188.234.247.110', '144.34.242.66', '182.72.142.62',
                                    '121.183.132.151', '43.154.174.101', '43.156.125.234', '125.141.139.9',
                                    '114.33.239.231', '46.101.254.194', '8.26.21.34', '156.232.6.68', '103.233.0.121',
                                    '134.209.175.24', '123.100.226.242', '144.24.210.121', '203.101.126.19',
                                    '43.154.50.6', '81.70.50.89', '104.225.150.138', '23.224.39.151', '147.182.141.153',
                                    '77.50.183.22', '192.241.236.30', '148.227.1.18', '114.34.229.236', '195.29.51.135',
                                    '102.164.61.62', '103.129.223.98', '43.154.147.127', '41.59.82.183',
                                    '106.13.85.194', '95.217.80.125', '20.226.46.159', '152.32.147.191',
                                    '159.65.118.84', '20.115.75.130', '196.43.103.254', '163.172.87.64',
                                    '157.230.42.195', '180.76.158.6', '106.13.142.37', '61.93.240.18', '20.65.71.2',
                                    '213.215.163.233', '86.164.17.162', '43.154.157.102', '185.74.5.184',
                                    '154.194.13.219', '47.176.38.242', '175.140.139.145', '137.184.197.218',
                                    '128.199.152.70', '108.179.217.233', '35.154.88.57', '43.154.42.83', '43.154.47.14',
                                    '111.175.1.54', '128.199.110.190', '43.154.69.93', '20.119.232.123', '125.77.23.30',
                                    '150.136.65.184', '178.18.252.186', '188.166.113.144', '92.205.21.38',
                                    '114.67.234.182', '115.75.146.156', '221.150.91.236', '143.244.190.237',
                                    '221.140.57.201', '45.7.196.67', '103.139.42.55', '43.156.123.181',
                                    '186.225.150.215', '43.155.90.59', '164.92.226.99', '60.210.40.210',
                                    '218.245.63.192', '43.156.125.191', '8.215.45.162', '138.201.109.89',
                                    '111.160.100.50', '104.236.17.54', '134.209.233.126', '62.113.108.169',
                                    '157.245.40.222', '120.48.2.61', '43.156.123.97', '200.7.198.66', '20.101.101.40',
                                    '103.146.140.24', '137.184.54.207', '167.99.158.168', '209.141.35.242',
                                    '83.0.66.35', '139.59.80.151', '102.130.114.226', '159.65.127.239',
                                    '103.145.143.202', '78.196.138.44', '103.140.18.90', '64.225.25.59',
                                    '121.65.121.149', '43.156.128.57', '95.71.13.224', '182.254.140.176',
                                    '118.32.30.34', '106.241.33.158', '50.225.176.238', '129.226.15.250',
                                    '180.76.138.143', '103.147.159.67', '93.184.10.249', '208.113.201.147',
                                    '41.160.238.202', '150.136.242.126', '37.156.146.163', '159.223.150.43',
                                    '211.43.12.240', '159.223.12.197', '1.234.58.214', '123.120.11.143',
                                    '43.156.123.250', '160.251.7.202', '120.224.163.253', '43.154.36.254',
                                    '162.243.146.147', '43.156.124.167', '43.154.89.83', '116.196.86.28',
                                    '43.154.188.244', '128.199.163.55', '43.154.5.129', '43.156.122.11',
                                    '128.199.143.246', '43.156.127.187', '128.116.154.5', '182.140.221.223',
                                    '43.156.123.191', '43.134.29.226', '178.62.111.142', '139.59.255.59', '43.134.1.59',
                                    '202.125.94.212', '62.210.207.22', '104.248.91.215', '220.180.112.208',
                                    '179.107.34.178', '185.217.127.171', '191.239.116.211', '122.160.51.88',
                                    '43.156.124.68', '62.201.207.53', '177.115.54.135', '116.247.81.99',
                                    '68.183.136.217', '167.99.137.141', '43.156.125.110', '64.227.6.223',
                                    '202.137.26.4', '167.172.50.98', '186.189.193.207', '68.183.212.10',
                                    '84.201.164.50', '43.154.118.34', '43.154.218.49', '87.237.233.14',
                                    '218.75.156.247', '128.199.115.255', '31.220.58.225', '193.151.134.158',
                                    '101.231.146.36', '64.227.44.140', '31.22.108.179', '165.232.190.76',
                                    '43.156.123.128', '106.12.185.16', '201.72.190.98', '154.73.36.7', '82.65.232.134',
                                    '111.67.199.217', '43.132.156.117', '68.183.80.221', '213.168.248.63',
                                    '43.154.233.68', '59.150.105.114', '110.185.85.117', '143.110.153.150',
                                    '165.232.140.100', '209.14.71.31', '159.65.97.125', '43.252.62.60',
                                    '192.210.207.67', '2.232.250.91', '120.92.111.55', '182.76.81.254', '120.48.22.163',
                                    '43.128.170.23', '43.128.4.194', '209.141.57.23', '20.123.235.249',
                                    '178.62.243.101', '23.95.80.57', '186.211.105.178', '43.129.211.157',
                                    '43.128.18.253', '69.49.245.238', '43.156.124.133', '187.216.254.180', '41.63.9.36',
                                    '23.105.219.71', '190.196.70.21', '68.168.142.91', '43.154.193.125',
                                    '200.16.132.42', '103.172.205.51', '102.128.78.42', '43.154.127.79',
                                    '103.102.42.42', '202.47.117.222', '104.248.123.197', '43.156.122.123',
                                    '128.199.26.132', '90.84.195.216', '177.44.208.107', '59.103.236.74',
                                    '134.209.8.231', '144.22.248.23', '43.154.60.161', '24.172.172.2', '167.235.54.246',
                                    '27.254.121.166', '150.185.5.105', '43.154.129.76', '180.232.70.125',
                                    '197.134.249.239', '128.199.19.74', '209.97.172.163', '43.133.44.86',
                                    '43.154.202.193', '101.231.146.34', '14.161.20.182', '35.185.183.125',
                                    '193.233.185.220', '210.114.18.28', '87.219.167.59', '118.70.233.231',
                                    '159.65.159.164', '217.92.15.51', '134.17.16.92', '51.75.224.152', '200.45.147.129',
                                    '203.240.232.56', '67.205.128.206', '178.62.215.237', '139.9.227.155',
                                    '152.32.193.111', '43.154.17.118', '43.154.63.36', '128.199.230.181',
                                    '181.47.29.254', '206.189.90.250', '171.244.139.237', '165.227.50.84',
                                    '165.227.124.168', '171.217.67.69', '51.222.205.124', '179.1.85.121',
                                    '43.154.188.69', '220.243.178.124', '103.133.57.242', '159.65.133.176',
                                    '118.69.82.233', '113.200.81.41', '43.155.113.19', '120.48.47.43', '167.99.89.94',
                                    '178.128.217.58', '206.189.233.23', '43.154.192.161', '178.20.41.108',
                                    '43.156.125.41', '162.243.73.244', '138.68.131.49', '202.67.9.54', '115.248.153.89',
                                    '103.233.2.22', '82.165.167.194', '184.96.190.11', '213.6.130.133', '47.52.39.76',
                                    '5.183.9.248', '43.154.158.237', '13.79.122.130', '36.153.118.90', '190.18.66.165',
                                    '43.155.63.124', '182.23.63.22', '37.139.16.229', '186.209.41.35', '154.94.4.209',
                                    '200.29.111.20', '35.199.95.142', '95.85.23.145', '103.144.245.66', '43.154.43.6',
                                    '157.245.101.171', '61.82.54.57', '94.23.27.28', '202.81.116.199', '217.172.68.37',
                                    '41.79.78.41', '43.156.123.106', '182.23.67.49', '157.245.100.238',
                                    '43.134.106.247', '159.65.138.77', '43.154.116.95', '78.92.219.157',
                                    '124.121.30.231', '147.182.188.81', '35.227.57.104', '134.122.8.241',
                                    '139.162.232.35', '181.235.104.2', '20.197.190.244', '75.119.145.61',
                                    '54.38.240.40', '5.58.8.4', '144.24.129.100', '43.154.67.173']

    def test_empty_log(self):
        self.assertEqual([], get_banned_ips(self.empty_log, True))
        self.assertEqual([], get_banned_ips(self.empty_log, False))

    def test_mini_log(self):
        self.assertSetEqual(set(self.mini_log_add_unbanned_expected_result), set(get_banned_ips(self.mini_log, True)))
        self.assertSetEqual(set(self.mini_log_expected_result), set(get_banned_ips(self.mini_log, False)))

    def test_log(self):
        self.assertSetEqual(set(self.log_add_unbanned_expected_result), set(get_banned_ips(self.log, True)))
        self.assertSetEqual(set(self.log_expected_result), set(get_banned_ips(self.log, False)))


if __name__ == '__main__':
    unittest.main()  # run all tests
