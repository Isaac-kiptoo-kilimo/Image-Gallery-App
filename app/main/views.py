
from importlib.resources import path
from flask import render_template,request,redirect,url_for,abort,flash,send_file
from . import main
# from ..requests import 
# from .forms import 
from ..models import User,Img
from .. import db,photos
from werkzeug.utils import secure_filename





# from flask_login import login_required,current_user

@main.route('/')
def index():
    images=Img.query.all()
    
    return render_template('main/index.html',images=images)

@main.route('/view_image')
def view_image():
    images=Img.query.all()
    
    return render_template('images/view_image.html',images=images)
    

@main.route('/upload',methods= ['GET','POST'])
def upload():
    # user = User.query.filter_by(username = uname).first()
    if request.method=='POST':

        f=request.files['photo']
        filename = secure_filename(f.filename)
        
        path = photos.save(f)
        print('photo name',path)
         
        # user.profile_pic_path = path
        mimetype=f.mimetype
        img=Img(img=path,mimetype=mimetype,imagename=filename)
        db.session.add(img)
        db.session.commit()
        
        return redirect(url_for('main.index'))
    return render_template('images/addimage.html')

@main.route('/images/singleimage/<int:id_img>')
def single_image(id_img):
    img=Img.query.filter_by(id=id_img).first()
    print('single image',img)
    return render_template('images/single.html',img=img)