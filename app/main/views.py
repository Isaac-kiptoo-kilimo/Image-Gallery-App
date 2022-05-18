from flask import render_template,request,redirect,url_for,abort,flash
from . import main
# from ..requests import 
# from .forms import 

from ..models import User,Image
from .. import db,photos

# from flask_login import login_required,current_user

@main.route('/')
def index():
    

    return render_template('main/index.html')

# ****************************************************************************************************************************#



@main.route('/upload-image',methods=['GET','POST'])

#@login_required
def upload_image():
    if request.method == 'POST':
        if request.files:
            image = request.files['image']
            
    return render_template('main/upload_image.html')
