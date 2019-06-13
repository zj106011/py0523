from flask import Blueprint
from App.models import Purchaser, Car
from App.settings import db

blue = Blueprint('blueprint',__name__)

@blue.route('/')
def index():
    return '欢迎使用Flask！'

@blue.route('/insertone/')
def insertone():
    p = Purchaser()
    p.name = 'Z公子'
    p.idcard = 'Z'
    p.sex = '男'

    db.session.add(p)
    #连接表,查询下一个是多少
    db.session.flush()
    # 获取插入的id
    print('===>',p.pid)
    db.session.commit()

    #作业
    #在主表中插入了一条数据,从表中插入一条
    return 'insert ok'

@blue.route('/getone/')
def getone():
    #以往我们继承的是Model对象
    #select * from Purchasers;
    # p = db.session.query(Purchaser)

    #迪卡尔积
    #select * from Purchaser,Car;
    # p = db.session.query(Purchaser,Car)

    #联表查询
    #select * from Purchaser inner join Car on Purchaser.pid = Car.pid;
    #join(主表,关联的字段)
    # p = db.session.query(Purchaser,Car).join(Purchaser,Purchaser.pid==Car.pid)
    # p = db.session.query(Purchaser, Car).outerjoin(Purchaser, Purchaser.pid == Car.pid)
    p = db.session.query(Purchaser,Car).filter(Purchaser.pid == Car.pid)
    print(len(list(p)))
    #自己实现left join
    # Purchaser_ = db.session.query(Purchaser)
    #
    # pids = [m.pid for m in Purchaser_]
    #
    # Car_ = db.session.query(Car).filter(Car.pid.in_(pids))
    #
    # #将两个数据融合到一起
    # #清理数据集
    # purs = []
    # for i in range(len(list(Purchaser_))):
    #     pur_dict = dict()
    #     # if Purchaser_[i].__dict__['_sa_instance_state'] != '_sa_instance_state';
    #     for k,v in Purchaser_[i].__dict__.items():
    #         if k != '_sa_instance_state':
    #             pur_dict[k] = v
    #     purs.append(pur_dict)
    #
    #
    # cars = []
    # for i in range(len(list(Car_))):
    #     car_dict = dict()
    #
    #     for k,v in Car_[i].__dict__.items():
    #         if k != '_sa_instance_state':
    #             car_dict[k] = v
    #     cars.append(car_dict)
    #
    # #cars添加两条空数据
    # num = len(purs) - len(cars)
    #
    # for i in range(num):
    #     sign = {}
    #     for k in cars[0].keys():
    #         sign[k] = None
    #     cars.append(sign)
    #
    # # print(cars)
    # #合并
    # result = []
    # for i in range(len(purs)):
    #
    #     for j in range(len(cars)):
    #         res = purs[i].copy()
    #         if purs[i]['pid'] == cars[j]['pid']:
    #             res.update(cars[j])
    #             result.append(res)
    #
    #
    # print(len(result))

    #子查询
    #selct * from Purchaser where pid in (select pid from Car where price >100000)
    # c = db.session.query(Car.pid).filter(Car.price > 1000000)
    # p = db.session.query(Purchaser).filter(Purchaser.pid.in_(c))
    # print(len(list(p)))

    return 'ok'






























