# fail2bangeolocation

Shows geolocation of failed attempts registered by *fail2ban*.  
It's useful to know from which locations you are being attacked the most.  
You can group locations by country or by country and by city.  

![GitHub repo file count](https://img.shields.io/github/directory-file-count/rubenhortas/fail2bangeolocation)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/rubenhortas/fail2bangeolocation)
![GitHub repo size](https://img.shields.io/github/repo-size/rubenhortas/fail2bangeolocation)

![PyPI](https://img.shields.io/pypi/v/fail2bangeolocation?&logo=pypi&logoColor=yellow)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fail2bangeolocation?logo=python&logoColor=yellow)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/fail2bangeolocation?logo=python&logoColor=yellow)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/fail2bangeolocation?logo=pypi&logoColor=yellow)
![PyPI - Downloads](https://img.shields.io/pypi/dm/fail2bangeolocation?&logo=pypi&logoColor=yellow)

![GitHub issues](https://img.shields.io/github/issues-raw/rubenhortas/fail2bangeolocation?logo=github)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/rubenhortas/fail2bangeolocation?logo=github)
![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/rubenhortas/fail2bangeolocation?&logo=github)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed-raw/rubenhortas/fail2bangeolocation?logo=github)
![GitHub all releases](https://img.shields.io/github/downloads/rubenhortas/fail2bangeolocation/total?logo=github)

![GitHub](https://img.shields.io/github/license/rubenhortas/fail2bangeolocation)

## Screenshots

* Grouped by country
<img src="https://github.com/rubenhortas/fail2bangeolocation/blob/main/screenshots/screenshot_grouped_by_country.png" alt="Output grouped by country" width="600">

* Grouped by country and city
<img src="https://github.com/rubenhortas/fail2bangeolocation/blob/main/screenshots/screenshot_grouped_by_country_and_city.png" alt="Output grouped by country and city" width="600">

## reallyfreegeoip.org

IP geolocation is done through [reallyfreegeoip.org](https://reallyfreegeoip.org). 
This means you will need an active internet connection in order to geolocate the IPs.

## Installation 

You can install *fail2bangeolocation* via *pipx*:

### Installation as user

```shell
$ pipx install fail2bangeolocation
```

### Installation as root

```shell
$ sudo su
# pipx install fail2bangeolocation
```

## Usage

* You can run *fail2bangeolocation* directly from the command line interface:

  ```shell
  fail2bangeolocation [-h] [-c] {fail2ban,log,server}
  ```

* *fail2bangeolocation* arguments

  ```shell
  usage: fail2bangeolocation.py [-h] [-c] {fail2ban,log,server} ...
  
  Shows geolocation of failed attempts registered by fail2ban
  
  positional arguments:
    {fail2ban,log,server}
                          These options are mutually exclusive
      fail2ban            analyze all banned IPs by fail2ban (from fail2ban output)
      log                 analyze a fail2ban log file. Use "log -h" to see more options
      server              analyze all banned IPs by fail2ban (e.g. "server sshd")
  
  optional arguments:
    -h, --help            show this help message and exit
    -c, --show-city       group IPs by country and city 
  ```

* ### Analyze all IPs registered by fail2ban 

  :warning: Requires root privileges  

  Run *fail2bangeolocation* using the *fail2ban* argument:

  ```shell
  $ sudo su
  # fail2bangeolocation fail2ban
  ```

* ### Analyze all IPs registered by fail2ban for a given jailed server/service, e.g. sshd 

  :warning: Requires root privileges  
  Run *fail2bangeolocation* with the *server* argument and the jailed server name:

  ```shell
  $sudo su
  # fail2bangeolocation server sshd
  ```

* ### Analyze a log file
  :warning: May require root privileges depending on the file to be analyzed  
  Run *fail2bangeolocation* with the *log* argument and the path to the log file:

  ```shell
  fail2bangeolocation log /var/log/fai2ban.log
  ```

  You can also geolocate the unbanned IPs contained in the log adding the **-u** argument:

  ```shell
  fail2bangeolocation log -u /var/log/fai2ban.log
  ```
  
* ### Group the output by country and city
  Run *fail2bangeolocation* with "**-c**" as first argument:

  ```shell
  fail2bangeolocation -c {fail2ban,log,server}
  ```
  
## Troubleshooting

In case of any problem, you create an [issue](https://github.com/rubenhortas/fail2bangeolocation/issues/new).

## Discussions
If you want ask (or answer) a question, leave an opinion or have an open-ended conversation you can create (or join) a [discussion](https://github.com/rubenhortas/fail2bangeolocation/discussions/new).

## Support

If you find this application useful you can star this repo.
