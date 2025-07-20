import mysql.connector
from flask import render_template, request, redirect, flash
from werkzeug.security import generate_password_hash
from database.db import get_db_connection
from . import auth_bp


@auth_bp.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        firstname: str = request.form["firstname"]
        lastname: str = request.form["lastname"]
        username: str = request.form["username"]
        password = request.form["password"]
        # debugger check input data
        # return Response(f"{username}")

        # """
        # validation
        if not username or not password:
            flash("All fields are required")
            return redirect("/registration")

        # hash the password
        hashed_pw = generate_password_hash(password)

        # Save to DB
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO registration (`firstname`, `lastname`, `username`, `password`) VALUES (%s, %s, %s, %s)",
                (firstname, lastname, username, hashed_pw),
            )
            conn.commit()
            flash("Registered Successfully!", "success")
        except mysql.connector.Error as err:
            flash(f"Error: {err}")
        finally:
            conn.close()
        return redirect("/registration")
    return render_template("pages/registration.html")


if __name__ == "__main__":
    auth_bp.run(debug=True)
