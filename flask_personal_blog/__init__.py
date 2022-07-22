from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from flask_personal_blog.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()


def init_app(config_class=Config):
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    from flask_personal_blog.mainapp.views import main
    from flask_personal_blog.postapp.views import posts
    from flask_personal_blog.userapp.views import users
    from flask_personal_blog.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(errors)

    db.create_all()

    return app
