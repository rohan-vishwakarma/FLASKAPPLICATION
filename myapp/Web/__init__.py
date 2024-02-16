from flask import Blueprint

Webappbp = Blueprint('webapp', __name__)


from myapp.Web import views
