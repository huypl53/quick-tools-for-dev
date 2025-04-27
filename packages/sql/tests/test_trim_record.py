from pathlib import Path
from sql.trim_record import process_large_sql_file, keep_records


def test_process_large_sql_file(tmp_path: Path):
    # Create a temporary SQL file
    sql_file = tmp_path / "test.sql"
    sql_file.write_text(
        "CREATE TABLE example (id INT, name TEXT);\n"
        "INSERT INTO example VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Extra'), (4, 'yolo'), (5, 'pacha');\n"
        "SELECT * FROM example;\n"
    )

    # Call the function and collect results

    results = "".join(
        list(
            process_large_sql_file(
                sql_file, kept_pattern=r"^(?!insert).*", filter_callback=keep_records
            )
        )
    )
    # print(results)
    # Assert the results
    assert results == (
        "CREATE TABLE example (id INT, name TEXT);\n"
        "INSERT INTO example VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Extra');\n"
        "SELECT * FROM example;\n"
    )
