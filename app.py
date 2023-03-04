from flask import Flask, render_template, redirect, url_for
from flask import request
from flask_wtf.csrf import CSRFProtect
from flask import make_response
from flask import flash
import forms
app = Flask(__name__)
app.config['SECRET_KEY']="Esta es la clave encriptada"
csrf=CSRFProtect()
# error 404------------------------------------------------------------------
@app.errorhandler(404)
def no_encontrada(e):
    return render_template('404.html'),404
@app.route("/cookies", methods=['GET','POST'])
def cookies():
    reg_user=forms.LoginForm(request.form)
    datos=''
    if request.method=='POST' and reg_user.validate():
        user=reg_user.username.data
        passw=reg_user.password.data
        datos=user+'@'+passw
        success_message='Bienvenido {}'.format(user)
        flash(success_message)

    response=make_response(render_template('cookies.html',form=reg_user))
    if len(datos)>0:
        response.set_cookie('datos_user',datos)
    return response
#------------------------------------------saludo 
@app.route("/saludo")
def saludo():
    valor_cookie=request.cookies.get('datos_user')
    nombres=valor_cookie.split('@')
    return render_template('saludo.html',nom=nombres[0])

#-------------------actividad 1 calidicaciones 

@app.route("/actividad1", methods=["GET", "POST"])
def iniciar():
    numero = 0
    num_form = forms.Numero(request.form)
    if request.method == 'POST':
        numero =  int(request.form.get("numero"))
    return render_template("formulariocalificaciones.html", num = numero, form = num_form)
    
@app.route("/resultado", methods=["POST"])
def generarResultado():
    elementos = request.form.getlist("num")
    for i in range(0, len(elementos)):
        elementos[i] = int(elementos[i])
    numMin = min(elementos)
    numMax = max(elementos)
    prom = sum(elementos)/len(elementos)
    duplicados = {}
    alertas = []
    for num in elementos:
        if num in duplicados:
            duplicados[num] += 1
        else:
            duplicados[num] = 1

    for num, cantidad in duplicados.items():
        if cantidad > 1:
            alertas.append("El número {} se repite {} veces.".format(num, cantidad))

    listResult = {'minimo': numMin, 
                  'maximo':numMax, 
                  'promedio': prom,
                  'listaRep': alertas
                  }
        
    return render_template('calificaciones.html', lista = listResult)

#----------------------------------------------------formulario alumnos
@app.route("/formulario")
def formulario():
    return render_template('formulario.html')

@app.route("/alumnos", methods=['GET','POST'])
def alumnos():
    alum_form=forms.UserForm(request.form)
    if request.method=='POST' and alum_form.validate():
        print(alum_form.matricula.data)
        print(alum_form.nombre.data)
    return render_template('Alumnos.html',form=alum_form)

# --------------------------traductor actividad 2
@app.route("/traductor", methods=['GET', 'POST'])
def traductor():
    form = forms.TraductorForm(request.form)
    form1 = forms.BuscarForm(request.form)
    if request.method == 'POST' and form.validate():
        espanol = form.espanol.data.lower()
        ingles = form.ingles.data.lower()
        f = open("traductor.txt", "a")
        f.write(f"{espanol},{ingles}\n")
        f.close()
        return redirect(url_for('traductor'))
    elif request.method == 'POST' and form1.validate():
        idioma = int(form1.idioma.data)
        index=0 if idioma==1 else 1
        palabra = form1.palabra.data.lower()
        f = open("traductor.txt", "r")
        palabras = f.readlines()
        f.close()
        palabra_traducida = "La palabra no está registrada"
        for p in palabras:
            words=p.split(',')
            word=words[idioma].strip()
            print(word)
            if palabra == word:
                palabra_traducida = p.split(',')[index]
                break
        return render_template("traductor.html", form=form, form1 = form1, traduccion = palabra_traducida)
    return render_template("traductor.html", form=form, form1 = form1)

@app.route("/", methods=["GET"])
@app.route("/diccionario", methods=["GET","POST"])
def Diccionario():
    diccionario=forms.Palabras(request.form)
    palabraIngles=''
    palabraEspaniol=''
    DICCIONARIO={
    "amarillo":"yellow",
    "casa":"house",
    "mesa":"table",
    "puerta":"door",
    }
    mat=diccionario.palabraIngles.data
    
    
    while request.method=='POST' and diccionario.validate():
        print (diccionario.palabraIngles.data)
        palabraIngles =  str(request.form.get("palabraIngles"))
        palabraEspaniol =  str(request.form.get("palabraEspaniol"))
    
        print (palabraIngles)
        print (palabraEspaniol)
        
        if DICCIONARIO.get(palabraIngles)==None:
            DICCIONARIO.update({palabraEspaniol:palabraIngles})
            print(DICCIONARIO)
            break
            
    return render_template("traductor.html", form=diccionario)

# resitencia ::::::------------------------------------------------
@app.route("/resistencia", methods=["GET", "POST"])
def resistencia():
    form = forms.Resistencias(request.form)
    b1=''
    b2=''
    b3=''
    cb1=''
    cb2=''
    cb3=''
    cbt=''
    tolerancia=0
    resultadox=0
    resultadoFMin=0
    resultadoFMax=0
    succes_message='Cálculo realizado con éxito'
    if request.method == 'POST' and form.validate():
        b1 = form.b1.data
        print(b1)
        if b1=='0':
            cb1='#000000'
        elif b1=='1':
            cb1='#9C640C'
        elif b1=='2':
            cb1='#FF0000'
        elif b1=='3':
            cb1='#D35400'
        elif b1=='4':
            cb1='#FEFF33'
        elif b1=='5':
            cb1='#5AFF33'
        elif b1=='6':
            cb1='#33A4FF'
        elif b1=='7':
            cb1='#D233FF'
        elif b1=='8':
            cb1='#8E8491'
        elif b1=='9':
            cb1='#FFFFFF'
        b2 = form.b2.data
        print(b2)
        if b2=='0':
            cb2='#000000'
        elif b2=='1':
            cb2='#9C640C'
        elif b2=='2':
            cb2='#FF0000'
        elif b2=='3':
            cb2='#D35400'
        elif b2=='4':
            cb2='#FEFF33'
        elif b2=='5':
            cb2='#5AFF33'
        elif b2=='6':
            cb2='#33A4FF'
        elif b2=='7':
            cb2='#D233FF'
        elif b2=='8':
            cb2='#8E8491'
        elif b2=='9':
            cb2='#FFFFFF'
        b3 = form.b3.data
        print(b3)
        if b3=='1':
            cb3='#000000'
        elif b3=='10':
            cb3='#9C640C'
        elif b3=='100':
            cb3='#FF0000'
        elif b3=='1000':
            cb3='#D35400'
        elif b3=='10000':
            cb3='#FEFF33'
        elif b3=='100000':
            cb3='#5AFF33'
        elif b3=='1000000':
            cb3='#33A4FF'
        elif b3=='10000000':
            cb3='#D233FF'
        elif b3=='100000000':
            cb3='#8E8491'
        elif b3=='1000000000':
            cb3='#FFFFFF'
        tolerancia = int(form.tolerancia.data)
        print(tolerancia)
        resultado=str(b1+b2)
        resultadox=int(int(resultado)*int(b3))
        print(resultado)
        print(resultadox)
        if tolerancia==1:
            resultadoFMin=float(float(resultadox)-float(resultadox)*0.05)
            resultadoFMax=float(float(resultadox)+float(resultadox)*0.05)
            print(resultadoFMin)
            print(resultadoFMax)
            cbt='#F4D03F'
        elif tolerancia==0:
            resultadoFMin=float(float(resultadox)-float(resultadox)*0.10)
            resultadoFMax=float(float(resultadox)+float(resultadox)*0.10)
            print(resultadoFMin)
            print(resultadoFMax)
            cbt='#A0A0A0'        
        flash(succes_message)
    response = make_response(render_template("resistencia.html", form = form,
                               b1=b1, b2=b2, b3=b3, tolerancia=tolerancia,
                               resultadoFMin=resultadoFMin, resultadox=resultadox,
                               resultadoFMax=resultadoFMax, cb1=cb1, cb2=cb2, cb3=cb3,
                               cbt=cbt))
    response.set_cookie('valor', str(resultadox))
    return response



if __name__== "__main__":
    csrf.init_app(app)
    app.run(debug = True)