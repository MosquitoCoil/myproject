from flask import redirect, session, request, flash, render_template
from database.db import get_db_connection
from . import auth_bp


# edit users
@auth_bp.route("/edit-user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if not session.get("is_admin"):
        flash("Access denied.")
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        username = request.form["username"]
        cursor.execute(
            "UPDATE registration SET firstname = %s, lastname = %s, username = %s WHERE id = %s",
            (firstname, lastname, username, user_id),
        )
        conn.commit()
        conn.close()
        flash("User updated successfully.")
        return redirect("/dashboard")

    cursor.execute("SELECT * FROM registration WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    conn.close()

    return render_template("admin/edit_user.html", user=user)


# delete users
@auth_bp.route("/delete-user/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    if not session.get("is_admin"):
        flash("Admin access only.", "error")
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM registration WHERE id = %s", (user_id,))
    conn.commit()
    conn.close()

    flash("User deleted successfully.", "success")
    return redirect("/users")
