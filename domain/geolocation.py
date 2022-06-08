import requests
import json


def get_geolocation_info(ip):
    # Result: {'country_code': 'JP', 'country_name': 'Japan', 'city': None, 'postal': None, 'latitude': 35.69,
    # 'longitude': 139.69, 'IPv4': '43.154.214.179', 'state': None}
    request_url = f'https://geolocation-db.com/jsonp/{ip}'
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result = json.loads(result)

    return result['country_name'], result['city']
