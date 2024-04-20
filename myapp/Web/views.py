from flask.views import MethodView, View
from flask import redirect, request, render_template, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import Session, session


from . import Webappbp
from .forms import ImageStorageForm
from myapp.Api.models import Images

from myapp import db

import requests


def profile():  
    if current_user.is_authenticated:
        return f'Hello, {current_user.username}'
    else:
        return None

def class_route(self, rule, endpoint, **options):

    def decorator(cls):
        self.add_url_rule(rule, view_func=cls.as_view(endpoint), **options)
        return cls

    return decorator

import base64
import urllib3
import requests

@Webappbp.route('/images/list', methods=['GET'])
def list_of_images():
    # Fetch all images from the database
    dictionary_response = {}
    images = Images.query.all()

    search_query = request.args.get('search')
    if search_query:
        try:
            header = {'Authorization': '08jrFeIXXDeJpBdYAgF8GcDuKm7sDTLc7rScWCWI56ArcoeR4Zl37xdw'}
            res = requests.get(f'https://api.pexels.com/v1/search?query={search_query}', headers=header, verify=False)
            if res.status_code == 200:
                dictionary_response = res.json()
        except Exception as e:
            print(e)

    return render_template('WEBAPP/imagelist.html', images=images, profile=profile(), dictionary_response=dictionary_response)



@class_route(Webappbp, "/images/list/<int:image_id>", "image_edit")
class ImageFormEdit(View):
    methods = ["GET", "POST"]
    
    @login_required
    def dispatch_request(self, image_id):
        image = Images.query.get_or_404(image_id)
        if request.method == "POST":
            db.session.delete(image)
            db.session.commit()            
            return redirect(url_for('webapp.list_of_images'))
        
        if request.method == "GET":
            return  render_template("WEBAPP/deleteimage.html", data = image)

@class_route(Webappbp, "/images", "images")
class ImageForm(View):
    methods = ["GET", "POST"]
    
    @login_required
    def dispatch_request(self):

        form = ImageStorageForm()
        if request.method == "POST":
            try:
                imagename = form.imagename.data
                image_file = form.image.data
                new_image = Images(imagename=imagename, image=image_file.read())
                db.session.add(new_image)
                db.session.commit()
            except Exception as e:
                print(str(e))
            finally:
                return redirect('/images/list')

        if request.method == "GET":
            form = ImageStorageForm()

            return render_template('WEBAPP/images.html', profile=profile(), form=form)



