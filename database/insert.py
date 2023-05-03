import _sqlite3

with _sqlite3.connect("database/app.db") as conn:

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios VALUES(?, ?)", (1, "Hola mundo"),
    )
