import persistencia
with open("pedidos.txt", "w", encoding="utf-8") as file:
 file.write("")
 file.close()

pedidos = [{"nombre": "Pedro", "apellidos": "Gil de Diego"},{"nombre": "Michael", "apellidos": "Jordan"}]
con=0

for pedido in pedidos:
        for nombre in pedido:
             valor = pedido.get(nombre)

             if(con==1):
                 con=0
                 persistencia.guardar_pedido(valor1,valor)
                 print("{}, {} ".format( valor1,valor))
             else:
                valor1= valor
                con= con+1
           
