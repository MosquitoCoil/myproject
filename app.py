from flask import Flask, render_template, Response
from auth import auth_bp
from sample.demo import test

app = Flask(__name__)
app.secret_key = "your secret key"

app.register_blueprint(auth_bp)


"""@app.route("/registration")
def register():
    return render_template("/pages/registration.html")


@app.route("/login")
def login():
    return render_template("/pages/login.html")"""


@app.route("/calculator")
def calculator():
    return render_template("/pages/calculator.html")


@app.route("/")
def home():
    return render_template("index.html")
    # return Response(test.trylang())


# import database connection checker
"""
@app.route("/")
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE()")
    db_name = cursor.fetchone()[0]
    conn.close()
    return f"Connected to database: {db_name}"
"""


if __name__ == "__main__":
    app.run(debug=True)
