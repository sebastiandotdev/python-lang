import _sqlite3

with _sqlite3.connect("database/app.db") as conn:

    cursor = conn.cursor()
    usuarios = [
        (2, "chanchito feliz"),
        (3, "chanchito triste")
    ]
    cursor.executemany(
        "INSERT INTO usuarios VALUES(?, ?)", usuarios,
    )
