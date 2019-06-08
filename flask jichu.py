
from flask import Flask, Response, json, make_response, render_template, url_for, request
from flask.json import jsonify
from  flask_script import  Manager
from werkzeug.utils import redirect
# shiliehua app
app=Flask(__name__)

# manager guanli bao
manager=Manager(app=app)

@app.route('/hello')
def hello_world():
    name=request.args.get('name','flask')

    return '<h1>hello %s</h1>'%name

@app.route('/abc/')
def index():
    return ('fuwuqifashengcuowu','gb')
# fanhui json duixiang
@app.route('/resjson/')
def resjson_():
    return Response(json.dumps({'name':'zhou','age':25}),content_type='application/json')
# fanhui jsonify
@app.route('/jsonif/')
def jsonif():
    return jsonify({'name':'zhoujie','age':18,'sex':'male'})

@app.route('/Makeres/')
def Makeres():
    return make_response(jsonify({'name':'zhoujie','age':18,'sex':'male'}),404)
# yin ru mo ban
@app.route('/reshtml/')
def reshtml():
    name='zhou'
    height=17
    add='chongqing'
    return render_template('index.html',name=name,height=height,add=add)

@app.route('/foo')
def foo():
    return '<h1> Foo Page<h1><a href="%s">Do somothing and redirect</a>' %url_for('do_something',next=request.full_path)
@app.route('/bar')
def bar():
    return '<h1> BAR Page<h1><a href="%s">Do somothing and redirect</a>' %url_for('do_something',next=request.full_path)
@app.route('/do_something')
# chongding xiang
def do_something():
    return redirect(request.args.get('next') ,url_for('hello'))


if __name__ == '__main__':
    app.run(debug=True)