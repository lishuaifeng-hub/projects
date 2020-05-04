from flask import Blueprint, views, render_template

bp = Blueprint("contact", __name__)


class Contact(views.MethodView):
    def get(self):
        return render_template("contact.html")


bp.add_url_rule("/contact", view_func=Contact.as_view("Contact"), endpoint="contact")
