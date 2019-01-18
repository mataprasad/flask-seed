from core.Application import Application
from app.resources.home import api as home_api
from core.Api import api
from app.views.home import bp as home_bp

flaskApp = Application(__name__)
flaskApp.register_blueprint(home_bp)
api.add_namespace(home_api)
