"""
Persistencia.
"""
def guardar_pedido(nombre,apellido):
    """guardar."""
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write("-" +nombre + " " + apellido + "\n")
        file.close()
    print("escritura exitosa")
