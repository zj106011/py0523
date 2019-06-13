from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app
from App.views import blue

app = create_app()
#注册manager
manager = Manager(app=app)

#注册migrate
manager.add_command('db',MigrateCommand)
#python manager.py db init  #生成一个migrations的目录,versions当中记录了迁移的表
#python manager.py db migrate #在数据库中生成 alembic_version的表,这个表会记录被创建的迁移文件的名称
#python manager.py db upgrede #生成表
#python manager.py db downgrede #删除表

#注册蓝图
app.register_blueprint(blueprint=blue)

if __name__ == '__main__':
    manager.run()