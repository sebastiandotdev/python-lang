import _sqlite3

conn = _sqlite3.connect("database/app.db")

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE if not exists usuarios
    (id INTENGER primary key, nombre VARCHAR(50));
    """
)
conn.commit()
conn.close()
