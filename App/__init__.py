from flask import Flask
from flask_cors import *

from App import settings
from App.LogManager.LoggingConfig import LOG_CONFIG
from App.ext import init_ext


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

    from .rest_v2 import rest_v2 as rest_v2_blueprint
    app.register_blueprint(blueprint=rest_v2_blueprint, url_prefix='/rest_v2')

    from .rest_v3 import rest_v3 as rest_v3_blueprint
    app.register_blueprint(blueprint=rest_v3_blueprint, url_prefix='/rest_v3')
    return app
