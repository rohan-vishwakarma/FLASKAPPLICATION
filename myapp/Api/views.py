
from flask import jsonify, request
from flask_restful import Resource
from flask_restful import reqparse
from sqlalchemy import exc



from myapp.Api import bp

@bp.route('/test')
def test_page():
    return 'Testing the Flask Application Factory Pattern'



def create_user(username, email, password):
    from myapp import db
    # Import the User model here
    from .models import User

    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()

def validate_user(username):
    from .models import User
    user = User.query.filter_by(username=username).count()

    if user == 1:
        return True

customer_args = reqparse.RequestParser()
customer_args.add_argument('username', type=str, help="username is required", location="form", required=True)
customer_args.add_argument('email', type=str, help="name of email is required", location="form", required=True)
customer_args.add_argument('password', type=str, help="password is required", location="form", required=True)
customer_args.add_argument('password2', type=str, help="Confirm password is required", location="form", required=True)

customers ={}


# from myapp.Api.models import User

class Customers(Resource):

    def get(self):
        from .models import User
        user = User.query.all()
        user_list =[{'id': users.id, 'username': users.username, 'email': users.email, 'created_at': users.created_at }  for users in user]
        
        return jsonify({'users': user_list})

    def post(self):

        try:
            args = customer_args.parse_args()
            uname = args['username']
            email = args['email']
            passwd = args['password']
            passwd2 = args['password2']

            if any([uname, email, passwd, passwd2]):
                validate = validate_user(uname)
                if validate == True:
                    return jsonify({'message' : f' Username {uname} alredy exist'})
                else:
                    if passwd != passwd2:
                        return jsonify({'message' : f' password doesnt match with {passwd2} '})
                    else:
                        create_user(uname, email, passwd)
                        return jsonify({'message' : 'Success'})          
            else:
                 return jsonify({'message' : 'please enter all fields'})                

                # user = User(username=uname, email=email, password=passwd)

        # except Exception as e:
        #     return jsonify({'messsage' : e}), 500
        
        except exc.SQLAlchemyError as e2:
            return jsonify({'messsage2' : e2}), 500
        except Exception as e:
            print(e)
    
        

        

        


        
    

