from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, EmailField
from wtforms.fields import TextAreaField
from wtforms import validators


class UserForm(Form):
    matricula=StringField("Matrícula",[validators.DataRequired(message='La matrícula es requerida')])
    nombre=StringField("Nombre", [validators.DataRequired(message='El campo es requerido'),validators.length
                                  (min=5, max=15, message="Nombre inválido")])
    Apaterno=StringField("Apaterno")
    Amaterno=StringField("Amaterno")
    email=EmailField("Correo")

class Numero(Form):
        num = StringField('numeros',      
                    [validators.data_required(message = 'Campo requerido')])
        
class Palabras(Form):
    palabraIngles=StringField("palabraIngles",[validators.DataRequired(message='La palabra en inglés es requerida')])
    palabraEspaniol=StringField("palabraEspaniol",[validators.DataRequired(message='La palabra en español es requerida')])