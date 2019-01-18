# add your own check function to the healthcheck
def mysql_available():
    return True, "mysql ok"