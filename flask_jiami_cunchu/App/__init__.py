from flask import Flask

from App.exts import init_ext


def create_app():
    app = Flask(__name__)
    init_ext(app)
    return app