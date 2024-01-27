from flask import Blueprint

celery_bp = Blueprint('celery_bp', __name__)


from myapp.redis_app import views
