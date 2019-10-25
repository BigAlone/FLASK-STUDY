# -*- coding: utf-8 -*-
# @File  : __init__.py.py
# @Author: Holly
# @Date  : 2019-08-28

from flask import Blueprint

rest = Blueprint('rest', __name__)
from flask_restful import Api

api = Api(rest)

from App.rest import views
