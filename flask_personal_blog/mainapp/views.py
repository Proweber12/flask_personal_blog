from flask import render_template, Blueprint

from flask_personal_blog.models import User

main = Blueprint('mainapp', __name__)


@main.route('/home')
@main.route('/')
def home():
    return render_template('index.html')
