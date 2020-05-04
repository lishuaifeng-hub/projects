from utils import db
from datetime import datetime
from flask_login import UserMixin


class User(db.Model,UserMixin):
    __tablname__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), doc='账户', nullable=False)
    password = db.Column(db.String(32), doc='密码', nullable=False)
    isAdmin = db.Column(db.Boolean, doc='是否管理员', default=False)
    create_time = db.Column(db.DateTime, default=datetime.now, nullable=False)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __str__(self):
        return "%s" % self.account
