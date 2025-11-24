
#------------Task 2 entrada de datos----------------#

# Se crea el ciclo while para cada variable con input para ingresar datos y su clase de variable utilizando True and Except, todo esto para que en caso
# de que el usuario ingrese un dato incorrecto, el sistema vuelve a solicitar el dato para continuar creand bucle

while True:
    try:
        nombre = str(input("ingresa el nombre del producto: "))
        break
    except ValueError:
        print("por favor ingresa un nombre válido")

while True:
    try:
        precio = float(input("escribe el precio: "))
        break
    except ValueError:
        print("por favor ingresa un valor nuevamente")

while True:
    try:
        cantidad = int(input("indica la cantidad: "))
        break
    except ValueError:
        print("por favor ingresa las unidades nuevamente")

#Se hace print para ensayar el type de cada una y uno general

print(type(nombre))
print(type(precio))
print(type(cantidad))

print(f"hola, el precio acordado para el producto {nombre} es {precio} para {cantidad} unidades, generando un total de {precio * cantidad} pesos")

# -----------------Task 3 operación matemática------#

#Se realiza la operación y se crea la variable de costo_total

costo_total = (precio * cantidad)
print(f"El costo total de tus productos es {costo_total} pesos")


# -----------------Task 4 operación matemática------#

#Se hace un print con las caracteristicas ingresadas en los datos

print(f"Producto: {nombre} / Precio: {precio} / Cantidad: {cantidad} / Total: {costo_total}")


#RESUMEN:

#   Este proyecto trata de desarrollar un programa en Python que 
#   permite registrar productos en un inventario, calculando automáticamente 
#   el costo total según el precio y la cantidad ingresados por el usuario.