from flask import Flask
from flask_cors import *

from App import settings
from App.ext import init_ext
from App.logging import LOG_CONFIG


def create_app(envname):
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config.from_object(settings.config.get(envname or 'default'))
    init_ext(app=app)

    from logging.config import dictConfig
    dictConfig(LOG_CONFIG)
    app.logger.name = 'app'

    from .main import main as main_blueprint
    app.register_blueprint(blueprint=main_blueprint, url_prefix='/')

    from .rest import rest as rest_blueprint
    app.register_blueprint(blueprint=rest_blueprint, url_prefix='/rest')
    return app
