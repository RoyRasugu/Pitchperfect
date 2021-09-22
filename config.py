import os

from flask_sqlalchemy import SQLAlchemy

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://royrasugu:qwerty@localhost/pitches'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USER_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    # '''
    # Production configuration child class

    # Args:
    #     Config: The parent configurattion class with General configuration settings
    # '''
    pass


class DevConfig(Config):
    # '''
    # Development configuration child class

    # Args:
    #     Config: The parent configuration class with General configuration settings
    # '''

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}