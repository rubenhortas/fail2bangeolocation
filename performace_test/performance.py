import timeit

from application import fail2banlog
from application.geolocation import _get_locations, _get_attempts, _sort, _sort_by_country, _sort_by_city


def _measure_time(function):
    t_start = timeit.default_timer()

    function()

    t_end = timeit.default_timer()
    t_total = (t_end - t_start)

    return f"{t_total:.10f} {function.__name__}"


if __name__ == '__main__':
    times = []
    log_file = 'fail2ban.log'
    add_unbaned = True
    baned_ips = fail2banlog.get_baned_ips(log_file, add_unbaned)
    locations, ips_not_found = _get_locations(baned_ips)
    attemtps = _get_attempts(locations)

    times.append(_measure_time(_sort_by_country(attemtps)))
    times.append(_measure_time(_sort_by_city(attemtps)))

    for time in times:
        print(f'{time}')
