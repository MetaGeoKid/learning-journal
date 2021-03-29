from flask_wtf import Form
from wtforms import TextAreaField, StringField, IntegerField, DateField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                               Length, EqualTo)


class PostForm(Form):
    title = StringField(validators=[DataRequired()])
    date = DateField("mm/dd/yyyy", format='%m/%d/%Y', validators=[DataRequired()])
    time_spent = IntegerField("How many hours did it take?", validators=[DataRequired()])
    content = TextAreaField("What did you learn?", validators=[DataRequired()])
    resources = TextAreaField("Who or what helped you learn?", validators=[DataRequired()])
