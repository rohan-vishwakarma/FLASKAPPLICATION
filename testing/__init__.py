import os
import sys
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_restful import Api as RestApi
from myapp.Api.views import Customers

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, logout_user
from flask_bcrypt import Bcrypt
from flask_session import Session
from flask import Flask, session
from flask_login import login_user, login_required, current_user


def profile():  
    if current_user.is_authenticated:
        return f'Hello, {current_user.username} '
    else:
        return None


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()
sess = Session()

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='static')
    app.config.from_object(config_class)
    app.config['BUNDLE_ERRORS'] = True
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"   
    bcrypt.init_app(app)
    sess.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'test_page'
    login_manager.login_message = "User needs to be logged in to view this page"
    login_manager.login_message_category = "warning"


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
        from myapp.Api.forms import LoginForm
        from myapp.Api.forms import SignUpForm

    
        app.register_blueprint(main_bp)
        app.register_blueprint(Mlbp)


        @login_manager.user_loader
        def load_user(user_id):
            print(user_id)
            return User.query.filter_by(email=user_id).first()
        
        @app.route('/get')
        def get():
            return session.get('username')


        
        @app.route('/', methods=['GET', 'POST'])
        def test_page():
            error = {}
            login_form = LoginForm()
            if request.method == "POST" and login_form.validate_on_submit():
                entered_password = request.form['password']
                user = User.query.filter_by(username=request.form['username']).first()
                if user:
                    password = user.password
                    id = user.id
                    check = bcrypt.check_password_hash(password, entered_password)
                    if check:
                        login_user(user)
                        error['message'] = f"Login Successfulll"
                        # session['username'] = request.form['username']
                    else:
                        error['message2'] = f"Invalid Password"
            return render_template('index.html',form=login_form , error=error, profile=profile())
    
            
        
        @app.route('/logout')
        def logout():
            logout_user()
            return redirect(url_for('test_page'))
        
        @app.route('/signup', methods=['POST', 'GET'])
        def signup():
            signup_form = SignUpForm()

            # if session.get("username"):
            #     return redirect(url_for('test_page'))
            if request.method == "POST" and signup_form.validate_on_submit():
                hashpassword = bcrypt.generate_password_hash(request.form['password']).decode('utf-8') 
                user = User(username=request.form['username'], 
                            email=request.form['email'],
                            password=hashpassword)
                db.session.add(user)
                db.session.commit()
                db.session.close()
                flash("User created Successfully", "success")
                return redirect(url_for('signup'))
              
            return render_template('signup.html', form=signup_form)


        

        @app.route('/Internal-server-error')
        def Internal_server_error():
            return render_template('error/sqlerror.html')
        

        with app.app_context():
            try:
                db.create_all()
                
            except Exception as e:
                print(e)
    
    return app
