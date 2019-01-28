from flask import Blueprint, render_template, request
from app.util.test import test
from core.util.db_util import __test_db_connection

bp = Blueprint('home-view', __name__)

@bp.route("/",methods=['GET','POST'])
def home():
    #__test_db_connection()
    data = []
    if request.method == 'POST':
        data = [ [request.form['resource_name']] ]
    return render_template("home.html",data=data)