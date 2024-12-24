import mysql.connector
import os
from contextlib import contextmanager

MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_USER = os.getenv('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'root_password')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'test_db')

@contextmanager
def get_connection():
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    try:
        yield conn
    finally:
        conn.close()