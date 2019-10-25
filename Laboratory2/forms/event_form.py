from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField
from wtforms import validators


class EditEvent(FlaskForm):
    name = StringField("name: ", [
        validators.DataRequired("Please enter your name.")

    ])

    user_id_fk = IntegerField("user_id_fk: ", [
        validators.DataRequired("Please enter your user_id_fk.")

    ])

    category = StringField("category: ", [
        validators.DataRequired("Please enter your category.")

    ])

    city = StringField("city: ", [
        validators.DataRequired("Please enter your city.")

    ])

    dates = DateField("date: ", [
        validators.DataRequired("Please enter your date.")

    ])

    price = IntegerField("price: ", [
        validators.DataRequired("Please enter your price.")

    ])

    hashtag = StringField("hashtag: ", [
        validators.DataRequired("Please enter your hashtag.")

    ])

    adress = StringField("adress: ", [
        validators.DataRequired("Please enter your adress.")

    ])

    submit = SubmitField("Save")
