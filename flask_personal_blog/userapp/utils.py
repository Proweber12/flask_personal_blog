import os
from secrets import token_hex

from flask import current_app, url_for
from flask_mail import Message
from PIL import Image

from flask_personal_blog import mail


def save_picture(form_picture):
    random_hex = token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, "static/profile_pics", picture_fn)

    output_size = (150, 150)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message("Запрос на сброс пароля", sender="poster24354@yandex.ru", recipients=[user.email])
    msg.body = f'Чтобы сбросить пароль, перейдите по следующей ссылке: {url_for("userapp.reset_token", token=token, _external=True)}. Если вы не делали этот запрос тогда просто проигнорируйте это письмо и никаких изменений не будет.'
    mail.send(msg)
