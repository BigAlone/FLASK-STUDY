# -*- coding: utf-8 -*-
# @File  : LogFormatter.py
# @Author: Holly
# @Date  : 2019-10-24
from flask import request
import logging


class RequestFormatter(logging.Formatter):
    def format(self, record):
        record.url = request.url
        record.remote_addr = request.remote_addr
        return super(RequestFormatter, self).format(record)


formatter = RequestFormatter(
    '{'
    '"asctime":"%(asctime)s",'
    '"levelname":"%(levelname)s",'
    '"funcName":"%(funcName)s",'
    '"filename": "%(filename)s",'
    '"lineno": "%(lineno)d",'
    '"url": "%(url)s",'
    '"remote_addr": "%(remote_addr)s",'
    '"thread": "%(thread)d",'
    '"threadName": "%(threadName)s",'
    '"message": "%(message)s"'
    '}'
)
