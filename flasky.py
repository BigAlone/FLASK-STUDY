# -*- coding: utf-8 -*-
# @File  : flasky.py
# @Author: Holly
# @Date  : 2019-10-15
from App import create_app
from App.ext import db
from App.model import example

app = create_app("develop")


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, example=example,db=db)
