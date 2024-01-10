import os
from flask import Flask, render_template
from flask_restful import Api as RestApi
from myapp.Api.views import Customers

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


    api = RestApi(app)
    api.add_resource(Customers, '/Api')


    # Initialize Flask extensions here

    # Register blueprints here
    from .Api import bp as main_bp
    from .MachineLearning import Mlbp

    app.register_blueprint(main_bp)
    app.register_blueprint(Mlbp)

    
    @app.route('/')
    def test_page():
        return render_template('index.html')

    return app
