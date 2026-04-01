from bs4 import BeautifulSoup


def parse_html(html: str) -> BeautifulSoup:
    """
    Parse raw HTML into a BeautifulSoup object.

    Args:
        html: Raw HTML string.

    Returns:
        BeautifulSoup parsed document.
    """
    return BeautifulSoup(html, "lxml")