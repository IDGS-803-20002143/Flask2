from flask import Flask, render_template
from flask import request
import forms

app=Flask(__name__)

@app.route("/formulario")
def formulario():
    return render_template("formulariocalificaciones.html")

@app.route("/Cali", methods=['GET', 'POST'])
def calificaciones():
    cali_form = forms.UserForm(request.form)
    if request.method == 'POST':
        print(cali_form.numero.data)
    return render_template("calificacion.html", form = cali_form)


if__name__="__main__"
app.run(debug=True)
