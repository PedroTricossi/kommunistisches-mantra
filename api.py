import flask
import os
from flask import jsonify
import psycopg2
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
DATABASE = os.getenv('DATABASE')
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


app = flask.Flask(__name__)
def get_db_connection():
    conn = psycopg2.connect(host=HOST,
                            database=DATABASE,
                            user=LOGIN,
                            password=PASSWORD)
    return conn


@app.route("/")
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM frases;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(books)


if __name__ == "__main__":
    app.run()