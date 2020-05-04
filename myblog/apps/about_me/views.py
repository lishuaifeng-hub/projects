# _*_encoding:utf-8_*_
from flask import Blueprint, views, render_template

bp = Blueprint("about", __name__)


class AboutMe(views.MethodView):
    def get(self):
        return render_template("about.html")


bp.add_url_rule("/about", view_func=AboutMe.as_view("AboutMe"), endpoint="about")
