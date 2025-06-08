from flask import Flask, render_template, request
import requests
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

student_url = f"{SUPABASE_URL}/rest/v1/student"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        programme = request.form['programme']
        hostel = request.form['hostel']

        data = {
            "name": name,
            "phone": phone,
            "programme": programme,
            "hostel": hostel
        }

        try:
            response = requests.post(student_url, json=data, headers=headers)
            if response.status_code == 201:
                return "Successfully added"
            else:
                print(f"Error: {response.status_code}, {response.text}")
                return "Error during database operation."
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {str(e)}")
            return "Error during database operation."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
