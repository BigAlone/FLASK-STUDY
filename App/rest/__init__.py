# -*- coding: utf-8 -*-
# @File  : __init__.py.py
# @Author: Holly
# @Date  : 2019-08-28

import logging

from flask import Blueprint

from App.LogManager.LogFormatter import requestformatter
from App.LogManager.LogHandler import LoggerHandlerToMysql
from App.settings import DevelopConfig

rest = Blueprint('rest', __name__)
from flask_restful import Api

api = Api(rest)
dblogger = logging.getLogger('Dblogger')
consolelog = logging.getLogger('StreamLogger')

SQLALCHEMY_DATABASE_URI = DevelopConfig.SQLALCHEMY_DATABASE_URI
LoggerHandler = LoggerHandlerToMysql(configdb_str=SQLALCHEMY_DATABASE_URI, table_name="example_log")
LoggerHandler.setFormatter(requestformatter)
dblogger.addHandler(LoggerHandler)

from App.rest import views
