from flask import Blueprint

# Don't set template_folder here, since we use the global templates folder
auth_bp = Blueprint("auth", __name__)

from . import edit_user, list_user, regAuth, loginAuth
