from flasgger import Swagger
from flask import Flask, url_for
from flask_cors import *

from App import settings
from App.LogManager.LoggingConfig import LOG_CONFIG
from App.ext import init_ext


def create_app(envname):
    app = Flask(__name__)
    Swagger(app)
    CORS(app, supports_credentials=True)
    app.config.from_object(settings.config.get(envname or 'default'))
    init_ext(app=app)

    from logging.config import dictConfig
    dictConfig(LOG_CONFIG)
    app.logger.name = 'app'

    from .main import main as main_blueprint
    app.register_blueprint(blueprint=main_blueprint, url_prefix='/')

    from .rest import rest as rest_blueprint
    app.register_blueprint(blueprint=rest_blueprint)

    return app
