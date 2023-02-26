from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, EmailField
from wtforms.fields import TextAreaField
from wtforms import validators

class Numero(Form):
        num = StringField('numeros',      
                    [validators.data_required(message = 'Campo requerido')])
from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, EmailField
from wtforms.fields import TextAreaField
from wtforms import validators


class Numero(Form):
        num = StringField('numeros',      
                    [validators.data_required(message = 'Campo requerido')])
        
