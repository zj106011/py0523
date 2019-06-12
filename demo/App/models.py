from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class User(db.Model):#db.Model chuangjian mo xing de yuan sheng fang fa
    uid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(32))
    page=db.Column(db.Integer)
    #xuyao jia shenme lie jiu zai zhe li jia

#cun fang shu ju mo xing