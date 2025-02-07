import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)
def init_db():
    conn = sqlite3.connect("form_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    conn.commit()
    conn.close()
def save_to_db(name, email):
    conn = sqlite3.connect("form_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()
@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        save_to_db(name, email)
        return render_template("result.html", name=name, email=email)
    return render_template("form.html")
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
