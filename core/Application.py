from flask import Flask
from core.HealthCheck import init_health_check, add_check, add_env_dump
from core.envdump.EnvApplicationData import application_data
from core.health.MySqlHealthCheck import mysql_available
from core.health.RedisHealthCheck import redis_available
from core.views.ping import bp as ping_bp
from core.resources.ping import bp as ping_json_bp
from core.Api import bp as bp_api
import logging
import json

class Application(Flask):
    def __init__(self, import_name, *args, **kwargs):
        super(Application, self).__init__(import_name, *args, **kwargs)
        self.register_blueprint(bp_api)
        self.register_blueprint(ping_bp)
        self.register_blueprint(ping_json_bp)
        add_check(mysql_available)
        add_check(redis_available)
        add_env_dump("application", application_data)
        init_health_check(self)
        @self.before_first_request
        def before_first_request():
            print("before_first_request() called 1")

        @self.before_request
        def before_request():
            print("before_request() called 2")

        @self.after_request
        def after_request(response):
            print("after_request() called 3")
            if response.is_json:
                d = json.loads(response.get_data())
                d['altered'] = 'this has been altered...GOOD!'
                response.set_data(json.dumps(d))
            return response