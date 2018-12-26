from wtforms import StringField, PasswordField, SubmitField, Form
from wtforms.validators import DataRequired, Length, Email

class RegistrationForm(Form):

    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=6)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])

    submit = SubmitField('Sign up')

class LoginForm(Form):

    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])

    submit = SubmitField('Log in')


