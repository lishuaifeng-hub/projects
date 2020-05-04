# _*_encoding:utf-8_*_
import pymysql
from flask import Flask
from flask_babelex import Babel
from flask_login import LoginManager
from apps.article import bp as article_bp
from apps.about_me import bp as about_bp
from apps.contact import bp as contact_bp
from apps.admins import admin
from utils import db


def create_app():
    app = Flask(__name__)
    app.register_blueprint(article_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(contact_bp)
    app.config.from_object('config')
    Babel(app)
    LoginManager(app)
    db.init_app(app)
    admin.init_app(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="127.0.0.1", port=5000, debug=True)
