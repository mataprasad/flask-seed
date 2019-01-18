from flask import Blueprint, render_template
from app.util.test import test
from core.util.db_util import __test_db_connection

bp = Blueprint('home-view', __name__)

@bp.route("/")
def home():
    __test_db_connection()
    return render_template("home.html",data=test())