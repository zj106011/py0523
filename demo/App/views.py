from flask import Blueprint, render_template, make_response, request, session
from werkzeug.utils import redirect
#lian jie M he T kongzhiqi shitu
from App.models import db, User

blue=Blueprint('blueprint',__name__)
@blue.route('/')
def index():
    return '123'
#she zhi cookie
# @blue.route('/login/')
# def login():
#     return render_template('login.html')

@blue.route('/logincookie/',methods=['post'])
def logincookie():
    #huoqu cookie
    # request.cookie.get('username','youke')
    # response=redirect() she zhi cookie
    account=request.form.get('account')
    response=redirect('/toindexcookie/')
    response.set_cookie('account',account)
    return response


@blue.route('/toindexcookie/')
def toindexcookie():
    # huoqu cookie
    # request.cookie.get('username','youke')
    # response=redirect()
    account=request.cookies.get('account','youke')
    return '<h1>huanyin %s denglu</h1>'%account +'<br/><a href="/delcookie/">tuichudenglu</a>'

@blue.route('/delcookie/')
def delcookie():
    response=redirect('/toindexcookie/')
    response.delete_cookie('account')
    return response


#session

#
# @blue.route('/demo.html/')
# def demo():
#     return render_template('demo.html')

# @blue.route('/for_/')
# def for_():
#     return '2'

# @blue.route('/createstudinfo')
# def createstudinfo():
#     return
#
# @blue.route('insertstudinfo')
# def insertstudinfo():
#     return
#
#

@blue.route('/session/')
def login():
    return render_template('login_session.html')

@blue.route('/loginsession/',methods=['get','post'])
def loginsession():
    account=request.form.get('account')
    response=redirect('/toindexsession/')
    session['account']=account
    return response

@blue.route('/toindexsession/')
def toindexsession():
    account=session.get('account','youke')
    return '<h1>huan ying %s deng lu>'%account + '<br/><a href="/loginout_session/">tuichu</a>'


@blue.route('/loginout_session/')
def loginout_session():
    response=redirect('/toindexcookie/')
    session.pop('account')if session.get('account')else 0
    return response
#
# @blue.route('/create_user/')
# def create_all():
#     db.create_all()
#     return 'ok'

@blue.route('/insert_user/')
def insert_user():
    user=User()#dui biao de mo xinf shi li hua



    user.__dict__.update({'name':'jack','page':20,'psex':'male'})
    user_ = User()
    user_.name = 'tom'
    user_.page = 18
    user_.psex='female'
    db.session.add_all([user_, user])
    db.session.commit()
    return 'quary ok'
# sqlalchemy-migrate shu ju mo xing qian yi
#Models hui ding yi hen duo de shu ju lei xing
#shi yong migrate hui
@blue.route('/checkpyflask/')
def checkpyflask():
    #zhi huo qu zhu jian ,fan hui mo xing de shi li
    # p=User.query.get(10)
    # p=User.query.first()
    # #huo qu suo you de,fan hui list leixing list mei yi ge yuan su dou shi mo xing de shi li
    # p=User.query.all()
    # #filter_by xiang dang yu where zhi neng shi = ,fanhui Basequery, ke die dai
    # p=User.query.filter_by(name='tom')
    # #filter
    # p=User.query.filter(User.page>=20)
    p=User.query.order_by(-User.page)

    print('>>>>>>>',p)
    print(type(p))
    return str(p[3].__dict__)


@blue.route('/getpage/')
def getpage():
    #ye ma 1 2 3 4,,,  page_num 10
    page=int(request.args.get('page'))
    page_num=10
    startpage=(page-1)*page_num

    #basequery dui xiang ,cun cu de mo xing duixiang
    users=User.query.offset(startpage).limit(page_num)
    return render_template('page.html',users=users,page=page)
