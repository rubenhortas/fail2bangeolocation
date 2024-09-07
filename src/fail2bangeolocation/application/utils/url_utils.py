from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from src.fail2bangeolocation.application.handlers.error_handler import handle_error
from src.fail2bangeolocation.crosscutting import strings


def is_online(url: str) -> bool:
    try:
        request = Request(
            url=url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        _ = urlopen(request).read()
        return True
    except HTTPError or URLError or OSError:
        handle_error(f"{url} {strings.IS_NOT_REACHABLE}", True)