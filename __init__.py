from flask import  Flask
from flask_session import  Session
from flask_sqlalchemy import  SQLAlchemy
from redis import Redis
def create_app():
    app=Flask(__name__)

    # app.config['SECRET_KEY']='10010'
    # app.config['SESSION_TYPE']='redis'
    # app.config['SESSION_REDIS']=Redis(host='127.0.0.1',port=6379,password='123456',db='12')
    # app.config['SESSION_KEY_PREFIX']='Flask'
    # # app.config.from_prfile(config.ini)
    # # app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root"mysql@127.0.0.1:3306/myflask?charset=utf8'
    # # app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=False
    # Session(app=app)#session chu shi hua
    return app
#
# app.__init__.db(app=app)