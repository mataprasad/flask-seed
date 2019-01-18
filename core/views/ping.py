from flask import Blueprint

bp = Blueprint('ping-view', __name__)

@bp.route("/ping")
def ping():
    return "Pong", 200