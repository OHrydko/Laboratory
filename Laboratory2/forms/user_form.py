from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField
from wtforms import validators


class EditUser(FlaskForm):
    name = StringField("name: ", [
        validators.DataRequired("Please enter your name.")

    ])

    surname = StringField("surname: ", [
        validators.DataRequired("Please enter your surname.")

    ])

    birthday = DateField("birthday: ", [
        validators.DataRequired("Please enter your birthday.")

    ])

    submit = SubmitField("Save")
