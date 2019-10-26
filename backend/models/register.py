from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    name = StringField("Name:", validators=[DataRequired()])
    location = StringField("Location:", validators=[DataRequired()])
    wars = StringField("Wars:", validators=[DataRequired()])
    properties = StringField("Properties:", validators=[DataRequired()])
    times = StringField("Times :", validators=[DataRequired()])

    def insert_data(self, celtic):
        self.name.data = celtic.name
        self.location.data = celtic.location
        self.wars.data = celtic.wars
        self.properties.data = celtic.properties
        self.times.data = celtic.times
