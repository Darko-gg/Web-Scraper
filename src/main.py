import argparse
from datetime import datetime
from pathlib import Path

from src.config import OUTPUT_DIR, DEFAULT_OUTPUT_FILENAME, DEFAULT_OUTPUT_FORMAT
from src.output.writer import write_json_file


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
        help="A single URL to process."
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

    return parser.parse_args()

def build_placeholder_result(args: argparse.Namespace) -> dict:
    """
    Build a placeholder result object for Step 1.
    """
    return {
        "status": "success",
        "message": "CLI is working. Scraping logic will be added in Step 2.",
        "timestamp": datetime.now().isoformat(),
        "input": {
            "url": args.url,
            "keyword": args.keyword
        },
        "output": {
            "filename": args.output,
            "format": args.format,
        }
    }

def main() -> None:
    args = parse_arguments()

    result = build_placeholder_result(args)

    output_path = OUTPUT_DIR / Path(args.output)

    if args.format == "json":
        write_json_file(result, output_path)
    else:
        raise ValueError(f"Unsupported format: {args.format}")
    
    print(f"Success: output written to {output_path}")


if __name__ == "__main__":
    main()