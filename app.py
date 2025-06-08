from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

# PostgreSQL connection using provided credentials
conn = psycopg2.connect(
    dbname="WASHINGTON",
    user="postgres",
    password="Bador",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        programme = request.form['programme']

        cursor.execute(
            "INSERT INTO students (name, phone, programme) VALUES (%s, %s, %s)",
            (name, phone, programme)
        )
        conn.commit()
        return redirect('/')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
