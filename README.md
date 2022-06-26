# fail2bangeolocation

Shows geolocation of failed attempts registered by *fail2ban*.  
It's useful to know from which locations you are being attacked the most.  
You can group locations by country or by country and by city.  

## Requirements

* python3
* fail2ban

## Installation 

You can run *fail2bangeolocation* directly, without installation, or you can install it via *pip3*:

```shell
$ pip3 install fail2bangeolocation
```

## Usage

* If you installed *fail2bangeolocation* with *pip3* you can run it directly from the command line interface:

```shell
$ fail2bangeolocation -h
```

* You can run *fail2bangeolocation* without installation calling the *fail2bangeolocation.py* script with *python3*

```shell
$ python3 fail2bangeolocation.py -h
```

* fail2bangeolocation arguments

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

:warning: Requires root privileges  

You can run it without parameters or using the *output* parameter:

```shell
$ fail2bangeolocation
```

```shell
$ fail2bangeolocation output
```

* ### Analyze all IPs registered by fail2ban for a given jailed server/service, e.g. sshd 

:warning: Requires root privileges

```shell
$ fail2bangeolocation server sshd
```

* ### Analyze a log file
:warning: May require root privileges depending on the file to be analyzed

```shell
$ fail2bangeolocation log /var/log/fai2ban.log
```

You can also geolocate the unbanned IPs contained in the log with the *-u* flag:

```shell
$ fail2bangeolocation log -u /var/log/fai2ban.log
```

## Troubleshooting

In case of any problem create an [issue](https://github.com/rubenhortas/fail2bangeolocation/issues/new)

## :star: Support

If you find this application useful you can star this repo.
