from flask import Blueprint

EmailSchedulingBp = Blueprint('emailschedulingbp', __name__, url_prefix='/email-scheduling')


from myapp.EmailScheduling import views
