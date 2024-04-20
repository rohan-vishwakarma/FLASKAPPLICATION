from flask.views import MethodView, View
from flask import request, render_template
from flask_login import login_required, current_user
from myapp.CeleryTask import addition

from . import EmailSchedulingBp


def profile():
    if current_user.is_authenticated:
        return f'Hello, {current_user.username}'
    else:
        return None


def class_route(self, rule, endpoint, **options):
    def decorator(cls):
        self.add_url_rule(rule, view_func=cls.as_view(endpoint), **options)
        return cls

    return decorator


@class_route(EmailSchedulingBp, "/", "/")
class Email(View):
    methods = ["GET", "POST"]
    @login_required
    def dispatch_request(self):
        if request.method == "POST":
            print("post")
            return "hello"

        if request.method == "GET":
            addition(12,13)
            return render_template('Email/index.html', profile=profile())
@EmailSchedulingBp.route('/add_email_address')
def add_email_address():
    return render_template('Email/add_email_address.html', profile=profile())

