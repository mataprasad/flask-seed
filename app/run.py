from core.Application import Application
from app.resources.home import api as home_api
from core.Api import api
from app.views.home import bp as home_bp
import logging
import json

flaskApp = Application(__name__)
flaskApp.register_blueprint(home_bp)
api.add_namespace(home_api)

@flaskApp.before_first_request
def before_first_request():
    print("before_first_request() called")
 
@flaskApp.before_request
def before_request():
    print("before_request() called")
 
@flaskApp.after_request
def after_request(response):
    print("after_request() called")
    if response.is_json:
        d = json.loads(response.get_data())
        d['altered'] = 'this has been altered...GOOD!'
        response.set_data(json.dumps(d))
    return response