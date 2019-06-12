from flask import  Flask
from flask_session import  Session
from flask_sqlalchemy import  SQLAlchemy
from App.exts import init_ext
def create_app():
    app=Flask(__name__)

    init_ext(app)
    # app.config.from_prfile(config.ini)
    # app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root"mysql@127.0.0.1:3306/myflask?charset=utf8'
    # app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=False
    # Session(app=app)#session chu shi hua

    #
    #mysql lianjie  mysql+driver//:username:password @host:post/db
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@127.0.0.1:3306/pyflask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db=SQLAlchemy()

    db.init_app(app=app)


    return app
#
# app.__init__.db(app=app)