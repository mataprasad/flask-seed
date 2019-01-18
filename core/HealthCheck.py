from healthcheck import HealthCheck, EnvironmentDump

checks = []
dumps = {}

def add_check(fnc):
        checks.append(fnc)

def add_env_dump(key, fnc):
        dumps[key] = fnc

def init_health_check(app):
    # wrap the flask app and give a heathcheck url
    health = HealthCheck(app, "/admin/healthcheck")
    envdump = EnvironmentDump(app, "/admin/environment")
    for check in checks:
        health.add_check(check)
    for dump in dumps:
        envdump.add_section(dump, dumps[dump])
