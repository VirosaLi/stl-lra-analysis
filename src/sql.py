import psycopg2

connection_str = "conn string"

with psycopg2.connect(connection_str) as conn:
    with conn.cursor() as curs:

        curs.execute(
            "CREATE TABLE IF NOT EXISTS test (HANDLE integer PRIMARY KEY, points double precision []);"
        )

        curs.execute(
            "INSERT INTO test (HANDLE, points) VALUES (%s, %s)",
            (2000002, [1, 2, 3, 4, 5, 6]),
        )

        curs.execute("SELECT * FROM test;")

        for record in curs:
            print(record)
