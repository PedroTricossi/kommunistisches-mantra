from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

HOST = os.getenv('HOST')
DATABASE = os.getenv('DATABASE')
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

def get_db_connection():
    conn = psycopg2.connect(host=HOST,
                            database=DATABASE,
                            user=LOGIN,
                            password=PASSWORD)
    return conn
