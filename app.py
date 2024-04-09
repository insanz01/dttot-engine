from flask import Flask
from flask_redis import FlaskRedis
from flask.blueprints import Blueprint
import api.routes

from api.utils.error_codes import ERROR_NOT_FOUND, ERROR_INTERNAL_SERVER_ERROR
from api.utils.response import response_error

app = Flask(__name__)
redis_client = FlaskRedis(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# Blueprints
app.url_map.strict_slashes = False
for blueprint in vars(api.routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint)


# Custom error pages
@app.errorhandler(404)
def not_found_error(error):
    return response_error('not found', ERROR_NOT_FOUND)


@app.errorhandler(500)
def internal_error(error):
    return response_error('internal error', ERROR_INTERNAL_SERVER_ERROR)


if __name__ == '__main__':
    app.run()
