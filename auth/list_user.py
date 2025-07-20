from flask import render_template, redirect, flash
from flask import session
from database.db import get_db_connection
from . import auth_bp


@auth_bp.route("/users")
def list_users():
    if not session.get("is_admin"):
        flash("Access denied.", "error")
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT id, firstname, lastname, username, timecreated FROM registration"
    )
    users = cursor.fetchall()
    conn.close()

    return render_template("admin/list_user.html", users=users)
