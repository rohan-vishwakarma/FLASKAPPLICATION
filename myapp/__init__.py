import os
from flask import Flask, redirect, render_template, url_for
from flask_restful import Api as RestApi
from myapp.Api.views import Customers

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['BUNDLE_ERRORS'] = True


    with app.app_context():


        db.init_app(app)
        migrate.init_app(app, db)
    
        api = RestApi(app)
        api.add_resource(Customers, '/Api')
        
        # Initialize Flask extensions here
    
        # Register blueprints here
        from .Api import bp as main_bp
        from .MachineLearning import Mlbp
        from myapp.Api.models import User
    
        app.register_blueprint(main_bp)
        app.register_blueprint(Mlbp)
    
        
        @app.route('/')
        def test_page():
            return render_template('index.html')
        

        @app.route('/Internal-server-error')
        def Internal_server_error():
            return render_template('error/sqlerror.html')
        

        with app.app_context():
            try:
                db.create_all()
            except Exception as e:
                print(e)
    
    return app
