#pei zhi wen jian ,pei zhi mysql

#
# from flask_sqlalchemy import SQLAlchemy
# db=SQLAlchemy()
# def user():
#     uid=db.Column(db.Integer ,primary_key=True,autoincrement=True)
#     name=db.Column(db.string(32))
#     age=db.Column(db.Interer)

def sqlalchemy_database_url(DATABASE):
    dialect =DATABASE['dialect']  or 'mysql'
    driver  =DATABASE['driver']   or 'pymysql'
    username=DATABASE['username'] or 'root'
    password=DATABASE['password'] or '123456'
    host    =DATABASE['host']    or '127.0.0.1'
    port    =DATABASE['port']   or '3306'
    database=DATABASE['database'] or 'pyflask'
    return "{}+{}://{}:{}@{}/{}".format(dialect,driver,username,password,host,port,database)
class Config():
    Test=False
    DeBug=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True#KE YI DA YIN LE
class DevelopConfig(Config):
    DeBug = True
    DATABASE={
        'dialect':'mysql',
        'driver':'pymysql',
        'username':'root',
        'password':'123456',
        'host':'127.0.0.1',
        'port':'3306',
        'database':'pyflask'
    }
    SQLALCHEMY_DATABASE_URI=sqlalchemy_database_url(DATABASE)

class TextConfig(Config):
    DeBug = True
    DATABASE={
        'dialect':'mysql',
        'driver':'pymysql',
        'username':'root',
        'password':'123456',
        'host':'127.0.0.1',
        'port':'3306',
        'database':'pyflask'
    }
    SQLALCHEMY_DATABASE_URI=sqlalchemy_database_url(DATABASE)


# class ShowConfig(Config):
#     DeBug = True
#     DATABASE={
#         'dialect':'mysql',
#         'driver':'pymysql',
#         'username':'root',
#         'password':'123456',
#         'host':'localhost',
#         'port':'3306',
#         'database':'0525'
#     }
#     SQLALCHEMY_DATABASE_URI=sqlalchemy_database_url(DATABASE)
#
# class ProConfig(Config):
#     DeBug = True
#     DATABASE={
#         'dialect':'mysql',
#         'driver':'pymysql',
#         'username':'root',
#         'password':'123456',
#         'host':'localhost',
#         'port':'3306',
#         'database':'0525'
#     }
#     SQLALCHEMY_DATABASE_URI=sqlalchemy_database_url(DATABASE)

#ding yi shu xing
ENV_NAME={
    'develop':DevelopConfig,
    'text':TextConfig
    # 'show':ShowConfig,
    # 'production':ProConfig
}