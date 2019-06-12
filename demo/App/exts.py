from flask_migrate import Migrate
from flask_session import  Session
from redis import Redis
from App.models import db
from App.setting import ENV_NAME



def init_ext(app):
    app.config['SECRET_KEY'] = '10010'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_REDIS'] = Redis(host='127.0.0.1', port=6379, db='14')
    app.config['SESSION_KEY_PREFIX'] = 'Flask'
    Session(app=app)
    # mysql

    app.config.from_object(ENV_NAME['develop'])

    db.init_app(app=app)
    #chu shi hua ming ling
    #python manager
    migrate = Migrate()
    migrate.init_app(app=app,db=db)

#kuozhang