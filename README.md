# fail2bangeolocation

Shows geolocation of failed attempts registered by fail2ban.  
It's useful to know from which locations you are being attacked the most.
You can group locations by country or by country and city.  

## Requirements

* python3
* fail2ban

## Installation 

You can run this application directly or install it via *pip3*

```shell
$ pip3 install fail2bangeolocation
```

## Usage

```shell
usage: fail2bangeolocation.py [-h] [-c] {output,log,server} ...

Shows geolocation of failed attempts registered by fail2ban

positional arguments:
  {output,log,server}  This options are mutually exclusive
    output             analyze all banned IPs by fail2ban (default without arguments).
    log                analyze a fail2ban log file. Use "log -h" to see more options.
    server             analyze all banned IPs by fail2ban (e.g. "server sshd")

optional arguments:
  -h, --help           show this help message and exit
  -c, --show-city      group IPs by country and city

```

* ### Analyze all IPs registered by fail2ban 

Requires root privileges
You can run it without parameters or using the *output* parameter:

```shell
$ fail2bangeolocation
```

```shell
$ fail2bangeolocation output
```

* ### Analyze all IPs registered by fail2ban for a given jailed server/service, e.g. sshd 

Requires root privileges

```shell
$ fail2bangeolocation server sshd
```

* ### Analyze a log file
May require root privileges depending on the file to be analyzed

```shell
$ fail2bangeolocation log /var/log/fai2ban.log
```

You can geolocate also the unbanned IPs contained in the log with the *-u* flag:

```shell
$ fail2bangeolocation log -u /var/log/fai2ban.log
```

## Troubleshooting

In case of any problem create an [issue](https://github.com/rubenhortas/fail2bangeolocation/issues/new)

## :star: Support

If you find this widget useful you can star this repo.
