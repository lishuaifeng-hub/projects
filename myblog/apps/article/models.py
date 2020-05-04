# _*_encoding:utf-8_*_
from utils import db
from datetime import datetime


class Author(db.Model):
    __tablname__ = "author"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    articles = db.relationship("Article", backref="author")
    create_time = db.Column(db.DateTime, default=datetime.now, nullable=False)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __str__(self):
        return "%s" % self.name


class Article(db.Model):
    __tablname__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    publish_time = db.Column(db.Date, default=datetime.now, onupdate=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __str__(self):
        return "%s" % self.title


# 一个分类对应多篇文章
class Category(db.Model):
    __tablname__ = "category"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), nullable=False)
    articles = db.relationship("Article", backref="category")
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __str__(self):
        return "%s" % self.name


#精选文章
class FeaturedArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"), nullable=False)
    article_title = db.relationship("Article", backref="featured",uselist=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __str__(self):
        return "%s" % self.id
