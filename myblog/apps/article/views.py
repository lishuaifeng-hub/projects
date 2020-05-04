# _*_ encoding:utf-8 _*_
from flask import Blueprint, views, render_template,request
from .models import Article, Category, FeaturedArticle

bp = Blueprint("articles", __name__)


class SplitPage:
    def split_page(self,page_num,total_pages):
        # 这部分是为了再有大量数据时，仍然保证所显示的页码数量不超过6，
        if page_num < 3:
            if total_pages <= 6:
                page_range = range(1, total_pages + 1)
            else:
                page_range = range(1, 7)
        elif (page_num >= 3) and (page_num <= total_pages - 3):
            page_range = range(page_num - 3, page_num + 3)
        else:
            page_range = range(total_pages - 5, total_pages + 1)
        return page_range


class IndexView(views.MethodView,SplitPage):
    def get(self):
        page_num = request.args.get("page",1,type=int)
        try:
            pagination = Article.query.order_by(Article.publish_time.desc()).paginate(page=page_num, per_page=6, error_out=True)
        except:
            pagination = Article.query.order_by(Article.publish_time.desc()).paginate(page=1, per_page=6, error_out=True)
        total_pages = pagination.pages
        page_range = self.split_page(page_num,total_pages)
        articles = pagination.items
        categories = Category.query.all()
        featured_articles = FeaturedArticle.query.all()
        return render_template('index.html',pagination=pagination,page_range=page_range,articles=articles,featured_articles=featured_articles,
        categories=categories)


class SingleArticle(views.MethodView):
    def get(self, article_id):
        article = Article.query.filter(Article.id == article_id).first()
        category = article.category
        categories = Category.query.all()
        featured_articles = FeaturedArticle.query.all()
        return render_template("single.html", article=article, featured_articles=featured_articles, category=category, categories=categories)


class CategoryView(views.MethodView,SplitPage):
    def get(self,category):
        page_num = request.args.get("page",1,type=int)
        category_id = Category.query.filter(Category.name==category).first().id
        try:
            pagination = Article.query.filter(Article.category_id==category_id).paginate(page=page_num, per_page=6, error_out=True)
        except:
            pagination = Article.query.filter(Article.category_id==category_id).paginate(page=page_num, per_page=6, error_out=True)
        articles = pagination.items
        total_pages = pagination.pages
        categories = Category.query.all()
        featured_articles = FeaturedArticle.query.all()
        page_range = self.split_page(page_num,total_pages)
        return render_template('category.html', pagination=pagination, page_range=page_range, articles=articles, featured_articles=featured_articles,
        category=category, categories=categories)


bp.add_url_rule("/", view_func=IndexView.as_view("IndexView"), endpoint="index")
bp.add_url_rule("/single/<article_id>", view_func=SingleArticle.as_view("SingleView"), endpoint="single")
bp.add_url_rule("/category/<category>", view_func=CategoryView.as_view("CategoryView"), endpoint="category")
