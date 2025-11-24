# ---------------------------------------------------------------
# Este archivo coordina el menú y la interacción con el usuario.
# Invoca funciones de servicios.py (CRUD, búsquedas, estadísticas)
# y funciones de archivos.py para guardar y cargar CSV.
# ---------------------------------------------------------------

from servicios import (
    agregar_producto, mostrar_inventario, buscar_producto, actualizar_producto,
    eliminar_producto, calcular_estadisticas
)
from archivos import guardar_csv, cargar_csv

import sys

def menu_principal():
    """Muestra el menú principal con todas las opciones disponibles."""
    print("""
---- Menú principal ----
1. Agregar producto
2. Mostrar inventario
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Estadísticas
7. Guardar CSV
8. Cargar CSV
9. Salir
------------------------
""")

def main():
    """
    Función principal que ejecuta el bucle del menú.
    Gestiona todas las operaciones del inventario.
    """
    inventario = []

    while True:
        menu_principal()
        opcion = input("Elige una opción (1-9): ").strip()
        if opcion not in [str(i) for i in range(1, 10)]:
            print("Opción inválida. Elige un número entre 1 y 9.")
            continue

        if opcion == "1":  # Agregar producto
            nombre = input("Nombre del producto: ").strip()
            if not nombre:
                print("Nombre requerido.")
                continue
            try:
                precio = float(input("Precio: ").strip())
                if precio < 0:
                    print("El precio no puede ser negativo.")
                    continue
            except ValueError:
                print("Precio inválido.")
                continue
            try:
                cantidad = int(input("Cantidad: ").strip())
                if cantidad < 0:
                    print("Cantidad no puede ser negativa.")
                    continue
            except ValueError:
                print("Cantidad inválida.")
                continue

            # Agregar o actualizar producto en inventario
            agregar_producto(inventario, nombre, precio, cantidad)
            print("Producto actualizado correctamente.")

        elif opcion == "2":  # Mostrar inventario
            mostrar_inventario(inventario)

        elif opcion == "3":  # Buscar producto
            nombre = input("Nombre a buscar: ").strip()
            prod = buscar_producto(inventario, nombre)
            if prod:
                print(f"Encontrado: {prod['nombre']} | Precio: {prod['precio']:.2f} | Cantidad: {prod['cantidad']}")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":  # Actualizar producto
            nombre = input("Nombre del producto a actualizar: ").strip()
            prod = buscar_producto(inventario, nombre)
            if not prod:
                print("Producto no encontrado.")
                continue
            print("Dejar vacío para no cambiar ese campo.")
            nuevo_precio_raw = input(f"Nuevo precio (actual {prod['precio']:.2f}): ").strip()
            nueva_cantidad_raw = input(f"Nueva cantidad (actual {prod['cantidad']}): ").strip()
            nuevo_precio = None
            nueva_cantidad = None
            if nuevo_precio_raw != "":
                try:
                    nuevo_precio = float(nuevo_precio_raw)
                    if nuevo_precio < 0:
                        print("Precio no puede ser negativo.")
                        continue
                except ValueError:
                    print("Precio inválido.")
                    continue
            if nueva_cantidad_raw != "":
                try:
                    nueva_cantidad = int(nueva_cantidad_raw)
                    if nueva_cantidad < 0:
                        print("Cantidad no puede ser negativa.")
                        continue
                except ValueError:
                    print("Cantidad inválida.")
                    continue
            # Actualiza producto con los valores ingresados
            actualizado = actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
            if actualizado:
                print("Producto actualizado.")
            else:
                print("No se pudo actualizar (producto no encontrado).")

        elif opcion == "5":  # Eliminar producto
            nombre = input("Nombre del producto a eliminar: ").strip()
            eliminado = eliminar_producto(inventario, nombre)
            if eliminado:
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "6":  # Mostrar estadísticas
            stats = calcular_estadisticas(inventario)
            print("\n--- Estadísticas ---")
            print(f"Unidades totales: {stats['unidades_totales']}")
            print(f"Valor total inventario: {stats['valor_total']:.2f}")
            pmc = stats['producto_mas_caro']
            if pmc:
                print(f"Producto más caro: {pmc['nombre']} - Precio: {pmc['precio']:.2f}")
            pms = stats['producto_mayor_stock']
            if pms:
                print(f"Producto con mayor stock: {pms['nombre']} - Cantidad: {pms['cantidad']}")
            print("--------------------")

        elif opcion == "7":  # Guardar inventario en CSV
            ruta = input("Ruta archivo destino: ").strip()
            if not ruta:
                print("Ruta inválida.")
                continue
            guardar_csv(inventario, ruta)

        elif opcion == "8":  # Cargar inventario desde CSV
            ruta = input("Ruta archivo a cargar (ej: inventario.csv): ").strip()
            if not ruta:
                print("Ruta inválida.")
                continue
            cargados, filas_invalidas = cargar_csv(ruta)
            if not cargados:
                print("No se cargaron productos.")
                continue

            print("\nFusión por defecto:")
            print("- Si el nombre ya existe: se suma la cantidad y se actualiza el precio al nuevo valor.")
            decision = input("¿Sobrescribir inventario actual? (S/N): ").strip().lower()
            if decision == "s":
                inventario = cargados
                accion = "Sobrescrito"
            else:
                # Fusionar productos cargados con inventario existente
                for p in cargados:
                    agregar_producto(inventario, p["nombre"], p["precio"], p["cantidad"])
                accion = "Fusionado"

            print(f"Resultado: {accion}. Productos cargados: {len(cargados)}. Filas inválidas omitidas: {filas_invalidas}")

        elif opcion == "9":  # Salir del programa
            print("Saliendo. ¡Hasta luego!")
            sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario. Saliendo.")