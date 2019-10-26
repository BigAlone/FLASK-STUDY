# coding: utf-8
import logging
from sqlalchemy import (Column, DateTime, Integer, MetaData,
                        String, Table, create_engine, Text)


class LoggerHandlerToMysql(logging.Handler):
    def __init__(self, configdb_str, table_name):
        # 连接数据库
        self.config_engine = create_engine(configdb_str)
        self.conn = self.config_engine.connect()
        metadata = MetaData(self.config_engine)
        # 创建数据表对象
        self.example_log = Table(table_name, metadata,
                                 Column('id', Integer, primary_key=True, autoincrement=True),
                                 Column('asctime', DateTime),
                                 Column('level_name', String(10)),
                                 Column('funcName', String(50)),
                                 Column('filename', String(50)),
                                 Column('url', String(100)),
                                 Column('addr', String(20)),
                                 Column('message', Text),
                                 Column('line_no', Integer))
        # 创建数据表
        metadata.create_all()
        logging.Handler.__init__(self)

    def emit(self, record):
        import datetime
        from flask import request
        try:
            message = record.msg
            ins = self.example_log.insert().values(
                asctime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                level_name=record.levelname,
                funcName=record.funcName,
                filename=record.filename,
                url=request.url,
                addr=request.remote_addr,
                message=str(message),
                line_no=record.lineno,
            )
            self.conn.execute(ins)
        except:
            pass

    def close(self):
        self.conn.close()

    def __del__(self):
        self.conn.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
