from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, SelectField, RadioField




class UserForm(Form):
    numero = StringField('numero')
    