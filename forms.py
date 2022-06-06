from wtforms import Form
from wtforms import StringField,TelField,DateField,EmailField,SelectField


class CommentForm(Form):
    nombre= StringField("nombre")
    apellidos=StringField("apellidos")
    fecha=DateField("fecha")
    numero=TelField("numero")
    dirrecion=StringField("direccion")
    tamano=SelectField("tamano")
    select=SelectField("select")

    #---------
    #@app.route("/prepara_pedido.html")
#def prepara():
 #   comment= forms.CommentForm(request.form)
  #  title= "Pizza FULL STACK"
   # return render_template("/prepara_pedido.html", title=title, form = comment)

#@app.route("/solicita_pedido.html")
#def solicita():
 #   title= "Solicitado correctamente"
  #  return render_template("/solicita_pedido.html", title=title)