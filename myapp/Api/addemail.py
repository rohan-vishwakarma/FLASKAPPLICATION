import sqlalchemy
from flask_restful import Resource
from flask import  jsonify, make_response
from flask_restful import reqparse
import json


emailparser = reqparse.RequestParser()
emailparser.add_argument('name', help='Name Cannot Be Empty', location="form",  required=True)
emailparser.add_argument('email', help='Name Cannot Be Empty', location="form", required=True)

def addEmail(name, email):
    try:
        from myapp import db
        from .models import Emails
        emailOBJ = Emails(name=name, email=email)
        db.session.add(emailOBJ)
        db.session.commit()
        return jsonify({"message" : "Email Created Successfully"}), 201
    except Exception as e:
        return output_json({"message": f"Something went Wrong", }, 500)

def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp

class AddEmail(Resource):
    def get(self):
        return jsonify({"Method": "Get Method"})
    def post(self):
        from myapp import db
        from .models import Emails
        addemail = emailparser.parse_args()
        name = addemail["name"]
        email = addemail["email"]
        try:
            user = Emails.query.filter_by(email=email).count()
            if user > 0:
                return output_json({"message": f"{email} Already Exist", }, 409)
            else:
                addEmail(name, email)
                return output_json({"message": f"{email} Created Successfully", }, 201)
        except Exception as e:
            return output_json({"message": f"Something Went Wrong", }, 500)

