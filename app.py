
from flask import Flask, request, redirect, Response

#from flask import render_template

#import forms

app = Flask(__name__)

@app.route("/pizza",methods=['POST'])
def render():
    print (request.form.get("nombre"))
    print (request.form.get("apellidos"))
    print (request.form.get("numero"))
    print (request.form.get("tamano"))
    print (request.form.get("select"))
    print (request.form.get("check"))

    return redirect("http://localhost/solicita_pedido.html")
       #comment= forms.CommentForm(request.form)
    #if request.method == "POST":
     #   print (comment.nombre.data )
      #  print (comment.apellidos.data) 
       # print (comment.fecha.data) 
        #print (comment.tamano.data)
        #print (comment.select.data ) 
@app.route("/checksize",methods=['POST'])
def checksize():
   """
   Comprueba disponibilidad de un tamaño de pizza.
   """
   val=request.form.get("tamano")
   if(val =="S"):
         mensaje="no disponible"
   mensaje=""
   return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})

