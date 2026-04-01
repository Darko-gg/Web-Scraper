from urllib.parse import urljoin

from bs4 import BeautifulSoup


def extract_title(soup: BeautifulSoup) -> str | None:
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return None


def extract_meta_description(soup: BeautifulSoup) -> str | None:
    meta_tag = soup.find("meta", attrs={"name": "description"})
    if meta_tag and meta_tag.get("content"):
        return meta_tag["content"].strip()
    return None


def extract_headings(soup: BeautifulSoup) -> dict:
    return {
        "h1": [tag.get_text(strip=True) for tag in soup.find_all("h1")],
        "h2": [tag.get_text(strip=True) for tag in soup.find_all("h2")],
        "h3": [tag.get_text(strip=True) for tag in soup.find_all("h3")],
    }


def extract_links(soup: BeautifulSoup, base_url: str) -> list[dict]:
    links = []

    for tag in soup.find_all("a", href=True):
        href = tag.get("href", "").strip()
        text = tag.get_text(strip=True)
        absolute_url = urljoin(base_url, href)

        links.append(
            {
                "text": text,
                "href": href,
                "absolute_url": absolute_url,
            }
        )

    return links


def extract_patagraphs(soup: BeautifulSoup) -> list[str]:
    paragraphs = []

    for tag in soup.find_all("p"):
        text = tag.get_text(" ", strip=True)
        if text:
            paragraphs.append(text)

        return paragraphs
    

def extract_page_data(soup: BeautifulSoup, base_url: str) -> dict:
    """
    Extract structed data from a parsed HTML document.
    """
    return {
        "title": extract_title(soup),
        "meta_description": extract_meta_description(soup),
        "headings": extract_headings(soup),
        "links": extract_links(soup, base_url),
        "paragraphs": extract_patagraphs(soup),
    }