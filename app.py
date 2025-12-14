from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Database config
db_config = {
    'user': 'root',
    'password': 'password',
    'host': 'db',
    'database': 'mydb'
}

@app.route('/')
def home():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        cursor.close()
        connection.close()
        return f"Database connected! Tables: {tables}"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)