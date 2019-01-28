from flask import Blueprint
from flask_restplus import Api

bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(bp,
    title='API',
    description='API'
)