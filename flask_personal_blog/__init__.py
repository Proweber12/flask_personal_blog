from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from flask_personal_blog.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager()
bcrypt = Bcrypt()


def init_app():
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from flask_personal_blog.mainapp.views import main
    from flask_personal_blog.postapp.views import posts
    from flask_personal_blog.userapp.views import users

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)

    db.create_all()

    return app
