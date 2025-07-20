from flask import render_template, request, redirect, flash, session
from werkzeug.security import check_password_hash
from database.db import get_db_connection
from . import auth_bp


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM registration WHERE username = %s", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):

            session["username"] = user["username"]
            session["is_admin"] = user["is_admin"]

            flash(
                f"Welcome, {user['firstname']}! Logged in at {user['timecreated']}",
                "success",
            )
            return redirect("/edit-user")
        else:
            flash("Invalid username or password.", "error")
            return redirect("/login")
    return render_template("pages/login.html")


@auth_bp.route("/dashboard")
def dashboard():
    if not session.get("user_id"):
        flash("You must be logged in.", "success")
        return redirect("/login")

    return render_template("admin/edit_user.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "success")
    return redirect("/login")


if __name__ == "__main__":
    auth_bp.run(debug=True)
