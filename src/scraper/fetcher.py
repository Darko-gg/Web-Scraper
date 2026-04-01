import certifi
import requests
import urllib3


DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}


def disable_insecure_request_warning() -> None:
    """
    Disable urllib3 warning for unverified HTTPS requests.
    Only use this when SSL verification is intentionally turned off.
    """
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def fetch_url(url: str, timeout: int = 10, verify_ssl: bool = True) -> tuple[str, int]:
    """
    Fetch raw HTML from a URL.

    Args:
        url: The target page URL.
        timeout: Request timeout in seconds.

    Returns:
        A tuple of (html_text, status_code)

    Raises:
        requests.RequestException: If the request fails.
    """
    verify_value = certifi.where() if verify_ssl else False

    if not verify_ssl:
        disable_insecure_request_warning()
    
    response = requests.get(
        url, 
        headers=DEFAULT_HEADERS, 
        timeout=timeout, 
        verify=verify_value
    )
    response.raise_for_status()
    return response.text, response.status_code