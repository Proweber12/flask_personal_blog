import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "site.sqlite")
    SECRET_KEY = "5791628bb0b13ce0c676dfde280ba245"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = "smtp.yandex.ru"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "poster24354@yandex.ru"
    MAIL_PASSWORD = "mumsojrzpjqlqbsw"
