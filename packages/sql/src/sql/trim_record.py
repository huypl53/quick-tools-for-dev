import re
from typing import Callable, Generator


def process_large_sql_file(
    file_path, kept_pattern=r"^insert", filter_callback: Callable = lambda x: x
) -> Generator[str, None, None]:
    """
    Processes a large SQL file line by line.

    Args:
        file_path (str): Path to the SQL file.
        kept_pattern (str): The regex pattern to match lines to be kept. Defaults to "^insert".
        filter_callback (Callable): A callback function to further filter or process lines. Defaults to a no-op lambda.

    Yields:
        str: Processed lines that match the kept pattern or pass the filter callback.
    """

    re_kept = re.compile(kept_pattern, re.IGNORECASE)
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            # Skip lines that don't contain 'insert'
            if re_kept.match(line.lower()):
                yield line
                continue

            if filter_callback:
                filtered_line = filter_callback(line)
                if not filtered_line:
                    continue
                yield filtered_line


# Define a filter callback to match content inside parentheses
def keep_records(line, up_to=3):
    import re

    prefix = " ".join(re.findall(r"^[^(]*", line))
    suffix = " ".join(re.findall(r"(?<=\))[^)]*$", line))

    matches = re.findall(r"\(.*?\)", line)
    return f"{prefix}{", ".join(matches[:up_to]) if matches else ""}{suffix}"
