from flask_wtf import Form
from wtforms import TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                               Length, EqualTo)


class PostForm(Form):
    title = TextAreaField(validators=[DataRequired()])
    date = TextAreaField("When did you learn something new?", validators=[DataRequired()])
    time_spent = TextAreaField("How many hours did it take?", validators=[DataRequired()])
    content = TextAreaField("What did you learn?", validators=[DataRequired()])
    resources = TextAreaField("Who or what helped you learn?", validators=[DataRequired()])
