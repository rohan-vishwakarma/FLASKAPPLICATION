from flask.views import MethodView, View
from flask import request, render_template
from flask_login import login_required

from . import Mlbp

def class_route(self, rule, endpoint, **options):

    def decorator(cls):
        self.add_url_rule(rule, view_func=cls.as_view(endpoint), **options)
        return cls

    return decorator

@class_route(Mlbp, "/machine-learning", "machine-learning")
class LinearRegression(View):
    methods = ["GET", "POST"]

    @login_required
    def dispatch_request(self):
        if request.method == "POST":
            print("post")
            return "hello"


        if request.method == "GET":
            return render_template('Ml/index.html')



