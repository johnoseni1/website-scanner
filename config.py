import os
from dotenv import load_dotenv
load_dotenv()


class Config:

    MONGO_URI = os.environ.get('MONGO_URI')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # setting mail configs
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("johnoseni26@gmail.com")
    MAIL_PASSWORD = os.environ.get("john*12345#")
    # app.config['MAIL_DEFAULT_SENDER'] = os.environ.get("MAIL_DEFAULT_SENDER")
