from flask_migrate import MigrateCommand

from App import create_app
from flask_script import Manager
from App.views import blue


app=create_app()
manager=Manager(app=app)
app.register_blueprint(blueprint=blue)


#liangge canshu ,diyige shi gei migrate qi ming zi
#di er ge canshu MigrateConmand
manager.add_command('db',MigrateCommand)
#chu shi hua ming ling
#python manager.py db init
#python manager.py db migrate  zai mysql zhong chuangjian yige innodb de biao,jilu mo xing zhong naxie biao yijing chuangjian
#python manager.py db upgrade zai shuju ku chuangjian biao zai alembic
#python manager.py db downgrade  zai shu ju ku zhong shan chu biao
if __name__ == '__main__':
    manager.run()
#qi dong bao ORM ru he feng zhuang yuanlei