from flask import Blueprint, render_template, make_response, request, session
from werkzeug.utils import redirect

blue=Blueprint('blueprint',__name__)
@blue.route('/')
def index():
    return '123'

@blue.route('/login/')
def login():
    return render_template('login.html')

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
#
#
# @blue.route('/loginsession/',methods=['get','post'])
# def loginsession():
#     account=request.form.get('account')
#     response=redirect('/toindexsession/')
#     session['account']=account
#     return response
#
# @blue.route('/toindexsession/')
# def toindexsession():
#     account=session.get('account','youke')
#     return '<h1>huan ying %s deng lu>'%account + '<br/><a href="/loginout_session/">tuichu</a>'
#
#
# @blue.route('/loginout_session/')
# def loginout_session():
#     response=redirect('/toindexcookie/')
#     session.pop('account')if session.get('account')else 0
#     return response