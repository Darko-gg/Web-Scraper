import json
from pathlib import Path


def write_json_file(data: dict, output_path: Path) -> None:
    """
    Write dictionary data to a JSON file.

    Args:
        data: The structured data to write.
        output_path: Full path to the output JSON file.
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)