# _*_encoding:utf-8_*_
from flask_admin.form import SecureForm
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from wtforms import TextAreaField
from wtforms.widgets import TextArea
from flask_login import current_user
from apps.article.models import Article, Author, Category, FeaturedArticle
from apps.user.model import User
from utils import db

class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class ArticleModelView(ModelView):
    column_list = ('id', 'title','desc','publish_time','author')
    column_labels = {
        'id':u'序号',
        'title' : u'文章标题',
        'desc' : u"文章描述",
        'publish_time' : u'发布时间',
        'author' : u'作者',
        'create_time' : u'数据入库时间',
        'update_time' : u'数据更新时间',
        'conent' : u'文章内容',
        'category' : u'类别'
    }
    column_editable_list = ['title',]

    form_excluded_columns = ['featured',]
    form_base_class = SecureForm
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']
    form_overrides = {
        'content': CKTextAreaField
    }

    can_create = True
    page_size = 5


class AuthorModelView(ModelView):
    page_size = 5


class CategoryModelView(ModelView):
    page_size = 5


class FeaturedArticleModelView(ModelView):
    page_size = 5

admin = Admin(name=u"后台管理管理系统",template_mode='bootstrap3')
admin.add_view(ArticleModelView(Article, db.session, name=u'文章管理',category=u"基础管理"))
admin.add_view(AuthorModelView(Author, db.session, name=u'作者管理',category=u"基础管理"))
admin.add_view(CategoryModelView(Category, db.session, name=u'类别管理',category=u"基础管理"))
admin.add_view(FeaturedArticleModelView(FeaturedArticle, db.session, name=u'精选文章',category=u"基础管理"))
