from flask import render_template,request,redirect,url_for,abort,flash
from . import main
# from ..requests import 
# from .forms import 
# from ..models import User
from .. import db,photos

# from flask_login import login_required,current_user

@main.route('/')
def index():


    return render_template('main/index.html')

@main.route('/upload-image',methods=['GET','POST'])
#@login_required
def upload_image(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
        return redirect(url_for('main.index',uname=uname))
    return render_template('main/upload_image.html')
