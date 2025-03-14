from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "flaskdb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")

def get_db_connection():
    connection = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return connection

@app.route("/")
def home():
    return jsonify(message="Hello from the Flask CI/CD project with PostgreSQL!")

@app.route("/db-test")
def db_test():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        cursor.close()
        connection.close()
        return jsonify(message="Connected to PostgreSQL!", version=db_version[0])
    except Exception as e:
        return jsonify(error=str(e))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)