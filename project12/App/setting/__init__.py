from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from App.setting.mysql_setting import ENV_NAME
from App.setting.session_setting import SESS

db = SQLAlchemy()

def return_settings(app):
    #1.session配置
    app.config.from_object(SESS)
    Session(app=app)

    #2.配置SQL
    app.config.from_object(ENV_NAME['develop'])
    db.init_app(app=app)