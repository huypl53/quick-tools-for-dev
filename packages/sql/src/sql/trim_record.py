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
            if re_kept.match(line.lower()):
                yield line
            else:
                filtered_line = filter_callback(line)
                if filtered_line:
                    yield filtered_line


def find_closing_paren(s: str, start: int) -> int:
    """Find the position of the matching closing parenthesis."""
    count = 1
    i = start
    while count > 0 and i < len(s):
        if s[i] == "(":
            count += 1
        elif s[i] == ")":
            count -= 1
        i += 1
    return i - 1 if count == 0 else -1


def keep_records(line, up_to=3):
    """
    Keep only up_to records from a SQL INSERT statement.
    Handles basic cases of missing parentheses.
    """
    if "VALUES" not in line:
        return line

    # Split the line at VALUES
    before_values, after_values = line.split("VALUES", 1)
    after_values = after_values.strip()

    # Find all value groups
    values = []
    current = ""
    paren_count = 0

    for char in after_values:
        if char == "(":
            paren_count += 1
            current += char
        elif char == ")":
            paren_count -= 1
            current += char
            if paren_count == 0:
                values.append(current.strip())
                current = ""
                if len(values) >= up_to:
                    break
        else:
            current += char

    # Handle any remaining value without closing parenthesis
    if current.strip():
        values.append(current.strip())

    # Take only up_to values
    values = values[:up_to]

    # Reconstruct the line
    return f"{before_values}VALUES {', '.join(values)};\n"
