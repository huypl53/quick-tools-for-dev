from pathlib import Path
from sql.trim_record import process_large_sql_file, keep_records


def test_process_large_sql_file(tmp_path: Path):
    # Create a temporary SQL file
    sql_file = tmp_path / "test.sql"
    sql_file.write_text(
        "CREATE TABLE example (id INT, name TEXT);\n"
        "INSERT INTO example VALUES (1, 'Alice'), (2, 'Bob is not good (not with everybody)'), (3, 'Extra (more than usual)'), (4, 'yolo'), (5, 'foo'), (6, 'bar');\n"
        "INSERT INTO example VALUES (1, 'Alice'), (2, 'Bob is not good (not with everybody)'), (3, 'Extra more than usual)'), (4, 'yolo'), (5, 'foo'), (6, 'bar');\n"
        "INSERT INTO example VALUES (1, 'Alice'), (2, 'Bob is not good (not with everybody)'), (3, 'Extra (more than usual'), (4, 'yolo'), (5, 'foo'), (6, 'bar');\n"
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
        "INSERT INTO example VALUES (1, 'Alice'), (2, 'Bob is not good (not with everybody)'), (3, 'Extra (more than usual)');\n"
        "INSERT INTO example VALUES (1, 'Alice'), (2, 'Bob is not good (not with everybody)'), (3, 'Extra more than usual)');\n"
        "INSERT INTO example VALUES (1, 'Alice'), (2, 'Bob is not good (not with everybody)'), (3, 'Extra (more than usual');\n"
        "SELECT * FROM example;\n"
    )
