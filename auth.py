# auth.py

from database import get_db_connection


def login(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        return True
    return False


def register(username, password):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
    except Exception as e:
        print("Error during registration:", e)
        return False
    finally:
        cursor.close()
        conn.close()
    return True
    return True
