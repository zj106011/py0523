from flask_migrate import Migrate

# from App.settings import return_settings, db
from App.settings import ENV_NAME,db

def init_ext(app):

    #引入数据库扩展,还有session的配置
    # return_settings(app)

    app.config.from_object(ENV_NAME['develop'])
    db.init_app(app=app)
    #配置migrate,正向迁移:把代码中的数据表模型给导入到数据库中


    migrate = Migrate()
    migrate.init_app(app=app,db=db)

    #把数据库中的表导入到代码中
    #codegen代码生成器
    #pip install flask-sqlacodegen
    #pymysql可以不写,但是默认的引擎是MySQLDB
    #flask-sqlacodegen  mysql+pymysql://root:123456@localhost:3306/project > App/models.py













