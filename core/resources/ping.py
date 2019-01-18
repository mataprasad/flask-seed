from flask import Blueprint, jsonify

bp = Blueprint('ping-json', __name__)

@bp.route("/ping.json")
def ping():
    return jsonify("Pong"), 200