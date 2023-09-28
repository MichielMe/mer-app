from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class MovieForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    director = StringField("Director")

    year = IntegerField("Year")
    
    submit = SubmitField("Add Movie")