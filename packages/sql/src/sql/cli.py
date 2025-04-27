import logging
import click


@click.group()
def sql_cli():
    """Trim SQL CLI"""
    pass


@click.option("--record-num", default=3, help="Number of records to keep")
@click.argument("file-out", type=click.Path(exists=False))
@click.argument("file-in", type=click.Path(exists=True))
@sql_cli.command()
def trim(record_num, file_in, file_out):
    """
    Trims a large SQL file by processing each line and keeping only the desired records.

    Args:
        record_num (int): The maximum number of records to keep from each line. Defaults to 3.
        file_in (str): Path to the input SQL file to be processed.
        file_out (str): Path to the output SQL file where the trimmed results will be saved.

    Behavior:
        - Processes the input SQL file line by line to avoid loading the entire file into memory.
        - Skips lines that do not match the specified pattern (e.g., lines not starting with "insert").
        - Extracts and keeps up to `record_num` records from lines that match the pattern.
        - Writes the processed results to the output file.
        - Logs warnings if the output file already exists and overwrites it.
    """
    from sql.trim_record import process_large_sql_file, keep_records
    import os
    if os.path.exists(file_out):
        logging.warning(f"File {file_out} already exists. Overwriting.")
    logging.info(f"Trimming SQL command from {file_in} to {file_out}")

    # Add your trimming logic here
    results = "".join(
        list(
            process_large_sql_file(
                file_in, kept_pattern=r"^(?!insert).*", filter_callback=keep_records
            )
        )
    )
    with open(file_out, "w", encoding="utf-8") as file:
        file.write(results)
    logging.info(f"Keeping {record_num} records")
    logging.info("SQL command trimmed")


@sql_cli.command()
def parse():
    """Parse SQL command"""
    logging.info("Parsing SQL command")
    # Add your parsing logic here
    logging.info("SQL command parsed")


def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("SQL CLI started")
    sql_cli()
    # Add your SQL CLI logic here
    # For example, connect to a database, execute queries, etc.
    logging.info("SQL CLI finished")
