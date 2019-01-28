from flask import Blueprint, request
from flask_restplus import Namespace, Resource

api = Namespace('home', description='Status related stuff')

parser = api.parser()
parser.add_argument('resource_name', type=str, help='Resource name', location='form')
parser.add_argument('attribute_name', type=str, help='Attribute name', location='form')
parser.add_argument('resource_value', type=str, help='Attribute value', location='form')
parser.add_argument('config_name', type=str, help='Config name', location='form')

@api.route("/")
class Home(Resource):
    @api.doc(parser=parser)
    def post(self):
        args = parser.parse_args()
        data = {'msg':"home "+ args['resource_name']}
        return data, 200
