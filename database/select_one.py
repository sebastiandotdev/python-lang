import _sqlite3

with _sqlite3.connect("database/app.db") as conn:

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    result = cursor.fetchone()
    print(result)
