# -*- coding: utf-8 -*-
# @File  : __init__.py.py
# @Author: Holly
# @Date  : 2019-08-28

from flask import Blueprint
from App.settings import DevelopConfig
from App.LogManager.LogFormatter import formatter
from App.LogManager.LogHandler import LoggerHandlerToMysql

rest = Blueprint('rest', __name__)
from flask_restful import Api

api = Api(rest)
import logging

logger = logging.getLogger('FileLogger')

SQLALCHEMY_DATABASE_URI = DevelopConfig.SQLALCHEMY_DATABASE_URI
LoggerHandler = LoggerHandlerToMysql(configdb_str=SQLALCHEMY_DATABASE_URI, table_name="example_log")
LoggerHandler.setLevel(logging.WARNING)
LoggerHandler.setFormatter(formatter)
logger.addHandler(LoggerHandler)
print(logger.handlers)
from App.rest import views
