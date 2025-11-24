#|---------------------------------------------------------|
#| Control de flujo y manejo de listas en el inventario    |
#|---------------------------------------------------------|
inventario = []


def agregar_producto():
    # Pide datos al usuario y agrega o actualiza un producto en la lista
    print("\n--- Agregar producto ---")

    # Validar si el nombre está vacío
    while True:
        nombre = input("Ingresa el nombre del producto: ").strip()
        if nombre == "":
            print("Debes ingresar un nombre, intenta de nuevo.")
        else:
            break

    # Validar precio y redondear a 2 decimales
    while True:
        entrada_precio = input("Ingresa el precio del producto: ").strip()
        try:
            precio = float(entrada_precio)
            if precio < 0:
                print("El precio debe ser positivo, intenta otra vez.")
            else:
                precio = round(precio, 2)
                break
        except ValueError:
            print("Precio invalido, debes ingresar un número.")

    # Validar cantidad
    while True:
        entrada_cantidad = input("Ingresa la cantidad de unidades solicitadas: ").strip()
        try:
            cantidad = int(entrada_cantidad)
            if cantidad < 0:
                print("Debes ingresar una cantidad positiva.")
            else:
                break
        except ValueError:
            print("Ingresa un número entero")

    # Si existe el producto, actualizar cantidad y precio
    for prod in inventario:
        if prod["nombre"].lower() == nombre.lower() and prod["precio"] == precio:
            prod["cantidad"] += cantidad
            prod["precio"] = precio
            print(f"Producto {prod['nombre']} actualizado. Cantidad: {prod['cantidad']} | Precio: {prod['precio']:.2f}")
            return

    # Si no existe, crear nuevo diccionario y agregarlo
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print(f"Producto {nombre} agregado correctamente.")


def mostrar_inventario():
    # Muestra todos los productos del inventario
    print("\n----Inventario Actual----")

    if len(inventario) == 0:
        print("El inventario está vacío.")
        return

    for i, prod in enumerate(inventario, start=1):
        print(f"{i}) Producto: {prod['nombre']} | Precio: {prod['precio']:.2f} | Cantidad: {prod['cantidad']}")


def calcular_estadisticas():
    # Calcula y muestra valor total del inventario y el total de unidades
    print("\n-----Estadísticas del Inventario-----")

    if len(inventario) == 0:
        print("No hay productos para calcular.")
        return

    valor_total = 0.0
    for prod in inventario:
        valor_total += prod["precio"] * prod["cantidad"]

    total_productos = sum(prod["cantidad"] for prod in inventario)
    productos_distintos = len(inventario)

    print(f"Valor total del inventario es: {valor_total:.2f}")
    print(f"Total de unidades registradas es: {total_productos}")
    print(f"Total de productos en el inventario es: {productos_distintos}")


# Bucle principal del menú
while True:
    print("""
    |--- Menú ---
    |1. Agregar producto
    |2. Mostrar inventario
    |3. Calcular estadísticas
    |4. Salir""")

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        calcular_estadisticas()
    elif opcion == "4":
        print("finalizando el programa...")
        break
    else:
        print("Opción inválida, intenta de nuevo.")

# -----------------------------------------------------------
# Comentarios
#
# realicé un menú interactivo para gestionar un inventario,
# permitiendo agregar productos, mostrarlos y calcular.
# Se usaron condicionales, bucles,
# listas, diccionarios y funciones para organizar el código.
# -----------------------------------------------------------