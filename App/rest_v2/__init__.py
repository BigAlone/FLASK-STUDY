# -*- coding: utf-8 -*-
# @File  : __init__.py.py
# @Author: Holly
# @Date  : 2019-08-28


from flask import Blueprint

from App.ext import api

rest_v2 = Blueprint('rest_v2', __name__)
api.init_app(rest_v2)
swg_api = api.namespace('home/home', description='Operations related to blog categories')
from App.rest_v2 import views
