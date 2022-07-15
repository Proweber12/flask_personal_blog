from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField("Заголовок", validators=[DataRequired()])
    content = TextAreaField("Текст поста", validators=[DataRequired()])
    submit = SubmitField("Отправить")
