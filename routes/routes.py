from flask import jsonify
from db.db_connection import get_db_connection

def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM frases;')
    frases = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(frases)

