from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    # Get distance data from the 10 latest rows
    cursor.execute("SELECT distance FROM distance ORDER BY id DESC LIMIT 10")
    distance_data = [row[0] for row in cursor.fetchall()]

    # Get motor status and fire detection status from the latest row
    cursor.execute("SELECT motor_status, fire_detect FROM distance ORDER BY id DESC LIMIT 1")
    motor_status, fire_detect = cursor.fetchone()

    conn.close()

    # Create a JSON data structure including distance, motor status, and fire detection status
    data = {
        "distance": distance_data,
        "motor_status": motor_status,
        "fire_detect": fire_detect
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
