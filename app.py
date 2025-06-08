from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

SUPABASE_URL = "https://oghgnfykbvbzuhvndcpc.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9naGduZnlrYnZienVodm5kY3BjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDkzNzgyMDgsImV4cCI6MjA2NDk1NDIwOH0.lOKu4dlxJkbcjpkvjNsjxm9lGIAA0ERc-jqJtXNTvnk"  # Replace with your actual anon key from the Supabase Dashboard

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

students_url = f"{SUPABASE_URL}/rest/v1/students"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        programme = request.form['programme']

        data = {
            "name": name,
            "phone": phone,
            "programme": programme
        }

        response = requests.post(students_url, json=data, headers=headers)

        if response.status_code == 201:
            print("Student added successfully")
            return redirect('/')
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return "Error during database operation."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
