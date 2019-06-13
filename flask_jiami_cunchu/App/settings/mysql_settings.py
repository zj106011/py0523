#配置mysql

def sqlalchemy_database_uri(DATABASE):
    dialect   =  DATABASE['dialect'] or 'mysql'
    driver    =  DATABASE['driver']  or 'pymysql'
    username  =  DATABASE['username']or 'root'
    password  =  DATABASE['password']or '123456'
    host      =  DATABASE['host']    or 'localhost'
    port      =  DATABASE['port']    or '3306'
    database  =  DATABASE['database']or 'project12'

    return "{}+{}://{}:{}@{}:{}/{}".format(dialect,driver,username,password,host,port,database)

class Config():
    Test = False
    DeBug = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class DevelopConfig(Config):
    DeBug = True
    DATABASE = {
        'dialect' : 'mysql',
        'driver'  : 'pymysql',
        'username': 'root',
        'password': '123456',
        'host'    : 'localhost',
        'port'    : '3306',
        'database': 'project12'
    }
    SQLALCHEMY_DATABASE_URI = sqlalchemy_database_uri(DATABASE)



class TestConfig(Config):
    DeBug = True
    DATABASE = {
        'dialect' : 'mysql',
        'driver'  : 'pymysql',
        'username': 'root',
        'password': '123456',
        'host'    : 'localhost',
        'port'    : '3306',
        'database': 'project12'
    }
    SQLALCHEMY_DATABASE_URI = sqlalchemy_database_uri(DATABASE)

ENV_NAME={
    'develop':DevelopConfig,
    'test'   :TestConfig
}