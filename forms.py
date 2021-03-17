from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, DateField, FloatField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                               Length, EqualTo)


class PostForm(Form):
    title = TextAreaField(validators=[DataRequired()])
    date = DateField(validators=[DataRequired()])
    time_spent = FloatField("How many hours?", validators=[DataRequired()])
    content = TextAreaField("What did you learn?", validators=[DataRequired()])
    resources = TextAreaField(validators=[DataRequired()])