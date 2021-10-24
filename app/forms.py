from wtforms import Form, BooleanField, StringField, PasswordField, validators, TextField


class ContactForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=120)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    message = StringField('Message')


