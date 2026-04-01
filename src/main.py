import argparse
from datetime import datetime
from pathlib import Path

import requests

from src.config import OUTPUT_DIR, DEFAULT_OUTPUT_FILENAME, DEFAULT_OUTPUT_FORMAT
from src.output.writer import write_json_file
from src.scraper.extractor import extract_page_data
from src.scraper.fetcher import fetch_url
from src.scraper.parser import parse_html


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments for the scraper tool.
    """
    parser = argparse.ArgumentParser(
        description="Web Scraper Tool - CLI entry point"
    )

    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "--url",
        type=str,
        help="A single URL to scrape."
    )
    input_group.add_argument(
        "--keyword",
        type=str,
        help="A keyword to search for."
    )

    parser.add_argument(
        "--output",
        type=str,
        default=DEFAULT_OUTPUT_FILENAME,
        help="Output filename. Default: results.json"
    )

    parser.add_argument(
        "--format",
        type=str,
        choices=["json"],
        default=DEFAULT_OUTPUT_FORMAT,
        help="Output format. Currently only supports json."
    )

    parser.add_argument(
        "--no-verify-ssl",
        action="store_true",
        help="Disable SSL certificate verification for troubleshooting only."
    )

    return parser.parse_args()



def scrape_single_url(url: str, verify_ssl: bool = True) -> dict:
    """
    Fetch, parse, and extract strusted data from a single URL.
    """
    html, status_code = fetch_url(url, verify_ssl=verify_ssl)
    soup = parse_html(html)
    page_data = extract_page_data(soup, url)

    return {
        "status": "success",
        "timestamp": datetime.now().isoformat(),
        "request": {
            "url": url,
            "mode": "url",
        },
        "response": {
            "status_code": status_code,
        },
        "data": page_data,
    }



def build_keyword_placeholder(keyword: str) -> dict:
    """
    Temporary placeholder until keyword mode is implemented.
    """
    return {
        "status": "success",
        "timestamp": datetime.now().isoformat(),
        "request": {
            "keyword": keyword,
            "mode": "keyword",
        },
        "message": "Keyword mode will be implemented."
    }



def main() -> None:
    args = parse_arguments()
    output_path = OUTPUT_DIR / Path(args.output)

    try:
        if args.url:
            result = scrape_single_url(
                args.url,
                verify_ssl=not args.no_verify_ssl
            )
        else:
            result = build_keyword_placeholder(args.keyword)

        if args.format == "json":
            write_json_file(result, output_path)
        else:
            raise ValueError(f"Unsupported format: {args.format}")
        
        print(f"Success: output written to {output_path}")

    except requests.RequestException as error:
        error_result = {
            "status": "error",
            "timestamp": datetime.now().isoformat(),
            "request": {
                "url": args.url,
                "keyword": args.keyword,
            },
            "error": str(error),
        }

        write_json_file(error_result, output_path)
        print(f"Request failed. Error written to {output_path}")


if __name__ == "__main__":
    main()