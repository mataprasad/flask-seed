from core.Application import Application
from app.resources.home import api as home_api
from core.Api import api
from app.views.home import bp as home_bp
import json

def before_request():
    print('From app 1')

def after_request(response):
    print('From app 2')
    if response.is_json:
        d = json.loads(response.get_data())
        d['altered'] = 'this has been altered...GOOD!'
        response.set_data(json.dumps(d))
    return response

flaskApp = Application(__name__,before_request,after_request)
flaskApp.register_blueprint(home_bp)
api.add_namespace(home_api)