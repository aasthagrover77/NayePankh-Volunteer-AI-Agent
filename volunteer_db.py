import sqlite3

def init_db():

    conn = sqlite3.connect("volunteers.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS volunteers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        interest TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_volunteer(name, email, interest):

    conn = sqlite3.connect("volunteers.db")
    c = conn.cursor()

    c.execute(
        """
        INSERT INTO volunteers(name,email,interest)
        VALUES(?,?,?)
        """,
        (name, email, interest)
    )

    conn.commit()
    conn.close()


def get_volunteers():

    conn = sqlite3.connect("volunteers.db")
    c = conn.cursor()

    c.execute("""
    SELECT name,email,interest
    FROM volunteers
    """)

    data = c.fetchall()

    conn.close()

    return data