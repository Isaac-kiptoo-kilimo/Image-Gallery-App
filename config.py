import os

class Config:
    # UPLOADED_PHOTOS_DEST ='app/static/photos'

    # API_KEY = os.environ.get('API_KEY')

    SECRET_KEY=os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URL')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:isaac@localhost/images'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    


# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:isaac@localhost/images'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql://fluqnrqxdkzffk:d90a0ab620ab8685368af495a722bdaf6e4633b2f77c4ef4dc29f1c008093092@ec2-44-195-169-163.compute-1.amazonaws.com:5432/deafursrrtnvs5'
    


class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:isaac@localhost/images'
    pass
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}
