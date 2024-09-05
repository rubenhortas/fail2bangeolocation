import json

import requests

# noinspection SpellCheckingInspection
REALLYFREEGEOIP_URL = 'https://reallyfreegeoip.org'


def get_location(ip: str) -> (str, str):
    # Response:
    # '{
    #   "ip":"207.188.187.163",
    #   "country_code":"US",
    #   "country_name":"United States",
    #   "region_code":"",
    #   "region_name":"",
    #   "city":"",
    #   "zip_code":"",
    #   "time_zone":"America/Chicago",
    #   "latitude":37.751,
    #   "longitude":-97.822,
    #   "metro_code":0
    #  }'
    try:
        request_url = f'{REALLYFREEGEOIP_URL}/json/{ip}'
        response = requests.get(request_url)
        result = response.content.decode()
        result = json.loads(result)

        return result['country_name'], result['city']
    except requests.RequestException:
        return None, None
