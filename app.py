from flask import Flask, render_template, request, redirect, flash, Response
import mysql.connector
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = "your secret key"

# MySQL DB config
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "myprojectdb",
}


def get_db_connection():
    return mysql.connector.connect(**db_config)


# @app.route("/")
# def registration():
# conn = get_db_connection()
# cursor = conn.cursor(dictionary=True)
# cursor.execute("SELECT * FROM registration")
# regitration = cursor.fetchall()
# conn.close()
# return render_template("/registration")


# Registration page
@app.route("/registration", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        username = request.form["username"]
        secret = request.form["secret"]
        # debugger check input data
        # return Response(f"{username}")

        # """
        # validation
        if not username or not secret:
            flash("All fields are required")
            return redirect("/registration")

        # hash the password
        hashed_pw = generate_password_hash(secret)

        # Save to DB
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO registration (`firstname`, `lastname`, `username`, `secret`) VALUES (%s, %s, %s, %s)",
                (firstname, lastname, username, hashed_pw),
            )
            conn.commit()
            flash("Registered Successfully!")
        except mysql.connector.Error as err:
            flash(f"Error: {err}")
        finally:
            conn.close()
        return redirect("/registration")
    return render_template("/pages/registration.html")
    # """


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
