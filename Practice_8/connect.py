import psycopg2
from psycopg2.extras import RealDictCursor
from config import config

def get_connection():
    conn = psycopg2.connect(**config)
    conn.autocommit = False
    return conn

def get_cursor(conn):
    return conn.cursor(cursor_factory=RealDictCursor)