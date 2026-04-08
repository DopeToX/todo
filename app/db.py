import psycopg
from psycopg.rows import dict_row

def get_connection():
    return psycopg.connect(
        host="db",
        dbname="todo",
        user="postgres",
        password="1234",
        row_factory=dict_row
    )

def get_cursor():
    conn = get_connection()
    return conn.cursor()