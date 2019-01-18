from flask import Blueprint
from flask_restplus import Namespace, Resource

api = Namespace('home', description='Status related stuff')

@api.route("/")
class Home(Resource):
    def get():
        return "home", 200
