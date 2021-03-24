from flask_wtf import Form
from wtforms import TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                               Length, EqualTo)


class PostForm(Form):
    title = TextAreaField(validators=[DataRequired()])
    date = TextAreaField(validators=[DataRequired()])
    time_spent = FloatField("How many hours?", validators=[DataRequired()])
    content = TextAreaField("What did you learn?", validators=[DataRequired()])
    resources = TextAreaField(validators=[DataRequired()])
