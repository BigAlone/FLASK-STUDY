def get_database_url(dbinfo):
    user = dbinfo.get("USER") or "root"
    password = dbinfo.get("PASSWORD") or "123456"
    host = dbinfo.get("HOST") or "locahost"
    port = dbinfo.get("PORT") or "3306"
    name = dbinfo.get("NAME") or "test"
    db = dbinfo.get("DB") or "mysql"
    driver = dbinfo.get("DRIVER") or "pymysql"
    return "{}+{}://{}:{}@{}:{}/{}".format(db, driver, user, password, host, port, name)


# 全局环境配置
class Config(object):
    # 是否开启debug
    DEBUG = False
    TESTING = False
    SECRET_KEY = "YOUR_SECRET_KEY"
    SESSION_TYPE = "sqlalchmey"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 开发环境配置N
class DevelopConfig(Config):
    DEBUG = True

    DATABASE = {
        "USER": "root",
        "PASSWORD": "zuber",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "zuber_log",
        "DB": "mysql",
        "DRIVER": "pymysql"
    }
    SQLALCHEMY_DATABASE_URI = get_database_url(DATABASE)


# 测试环境配置
class TestingConfig(Config):
    TESTING = True

    DATABASE = {
        "USER": "user_name",
        "PASSWORD": "user_pwd",
        "HOST": "your_host",
        "PORT": "your_database_port",
        "NAME": "db_name",
        "DB": "db_type",
        "DRIVER": "db_engine"
    }
    SQLALCHEMY_DATABASE_URI = get_database_url(DATABASE)


# 演示环境配置
class DemoConfig(Config):
    DEBUG = True

    DATABASE = {
        "USER": "user_name",
        "PASSWORD": "user_pwd",
        "HOST": "your_host",
        "PORT": "your_database_port",
        "NAME": "db_name",
        "DB": "db_type",
        "DRIVER": "db_engine"
    }
    SQLALCHEMY_DATABASE_URI = get_database_url(DATABASE)


# 线上环境-生产环境配置
class ProductConfig(Config):
    DATABASE = {
        "USER": "user_name",
        "PASSWORD": "user_pwd",
        "HOST": "your_host",
        "PORT": "your_database_port",
        "NAME": "db_name",
        "DB": "db_type",
        "DRIVER": "db_engine"
    }
    SQLALCHEMY_DATABASE_URI = get_database_url(DATABASE)


config = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "demo": DemoConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}
