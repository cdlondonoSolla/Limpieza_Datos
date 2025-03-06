def imprimir(paises):
    for pais in paises:
     print(pais, paises[pais])

paises = {
   "Argentina":40000000,
   "España":740000000,
   "Colombia":80000000,
   "Rusia":60000000,
   "Alemania":10000000,
   "Francia":50000000,
}

#imprimir(paises)

"""
Crear un diccionario que permita almacenar 5 articulos,
utilizar como clave el nombre del producto y como valor el precio del mismo.
Desarrollar ademas:
1) Imprimir en forma completa el diccionario OK
2) Imprimir solo los articulos con precio superior a 100.
"""

productos = {}
productosAlto = {}
producto = []
valor = []

def ingresar_producto():
   
    for i in range(5):
        print(f'{i+1}). Ingrese un producto')
        producto_input = str(input("Ingrese un producto: "))
        valor_input = int(input("Ingrese precio del producto: "))
        producto.append(producto_input)
        valor.append(valor_input)

    for i in range(len(producto)):
        productos[producto[i]] = valor[i]



def producto_def(productos):
    print('\nArticulos Ingresados:')
    for producto in productos:
        print(f'Nombre: {producto} Valor: {productos[producto]}') 
    
def valor_alto(productos):
    print('\nValores mayores a 100: ')
    for producto, valor in productos.items():
        if valor > 100:
            print(f'Nombre: {producto} Valor: {valor}')
 
    
    
ingresar_producto()
producto_def(productos)
valor_alto(productos)
