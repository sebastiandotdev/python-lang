import _sqlite3

with _sqlite3.connect("database/app.db") as conn:

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTENGER primary key, nombre VARCHAR(50));
        """
    )
