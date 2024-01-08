from flask import Blueprint

Mlbp = Blueprint('ml', __name__)


from myapp.MachineLearning import views
