# 配置第3方库-插件
from flask_migrate import Migrate
from flask_restplus import Api
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
api = Api(version='v1.0',title="swagger doc",description="关于项目中接口生成的文档")


def init_ext(app):
    db.init_app(app)
    Session(app=app)
    api.init_app(app)
    migrate.init_app(app=app, db=db)
