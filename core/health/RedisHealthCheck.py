# add your own check function to the healthcheck
def redis_available():
    return True, "redis ok"