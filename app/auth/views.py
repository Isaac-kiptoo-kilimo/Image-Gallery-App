from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user,logout_user,login_required
# from ..models import User,Wallet,Transaction
from .forms import LoginForm,SignupForm
from .. import db
from . import auth
from ..models import User

@auth.route('/auth/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "login"
    return render_template('auth/login.html',form = login_form)

@auth.route('/auth/signup',methods = ["GET","POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
      
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/signup.html',form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
