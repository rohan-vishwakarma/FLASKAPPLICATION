
from flask import jsonify, request
from flask_restful import Resource
from flask_restful import reqparse
from . import bp

@bp.route('/test')
def test_page():
    return 'Testing the Flask Application Factory Pattern'


customer_args = reqparse.RequestParser()
customer_args.add_argument('name', type=str, help="name of customer is required", location="form", required=True)
customer_args.add_argument('email', type=str, help="name of email is required", location="form", required=True)
customer_args.add_argument('city', type=str, help="name of city is required", location="form", required=True)

customers ={}


class Customers(Resource):

    def get(self):
        return {'hello': 'world'}

    def post(self):
        args = customer_args.parse_args()
        name = args['name']
        email = args['email']
        city = args['city']

        if any([name, email, city]):
            return jsonify({
                'message' : "All fields are not empty"
            })
        

        


        
    

