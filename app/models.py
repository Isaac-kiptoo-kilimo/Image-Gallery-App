
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from . import db
from datetime import datetime

   
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    bio = db.Column(db.String(1000))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), default=True)
    admin = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    images = db.relationship('Img', backref='user', lazy=True)
    reviews = db.relationship('Review', backref='user', lazy=True)

    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    def __repr__(self):
      return self.fullname




class Img(db.Model):
    __tablename__= 'images'
    id=db.Column(db.Integer,primary_key=True)
    img=db.Column(db.Text,unique=True,nullable=False)
    mimetype=db.Column(db.Text)
    title=db.Column(db.String(255))
    imagename=db.Column(db.Text)
    content=db.Column(db.Text)
    size=db.Column(db.Integer)  
    # category_id=db.Column(db.Integer,db.ForeignKey("categories.id"))
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    posted_at=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
      return self.imagename

# class Category(db.Model):
#     __tablename__= 'categories'
#     id=db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
#     updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
#     images=db.relationship('Img', backref='images', lazy=True)
    

#     def __repr__(self):
#       return self.name

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    image_id = db.Column(db.Integer)
    image_title = db.Column(db.String)
    image_path = db.Column(db.String)
    image_review = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    posted = db.Column(db.DateTime,default=datetime.utcnow)

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(image_id=id).all()
        return reviews

    def __repr__(self):
        return self.image_title


