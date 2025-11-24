# -----------------------------------------------------------------------------
# Funciones para operaciones CRUD y estadísticas sobre el inventario en memoria
# -----------------------------------------------------------------------------

from typing import List, Dict, Optional

def agregar_producto(inventario: List[Dict], nombre: str, precio: float, cantidad: int) -> None:
    """
    Agrega un producto al inventario.
    Si ya existe, suma la cantidad y actualiza el precio.
    Parámetros:
    inventario (List[Dict]): lista de productos
    nombre (str): nombre del producto
    precio (float): precio del producto
    cantidad (int): cantidad a agregar
    Retorno:
    None
    """

    nombre_clean = nombre.strip()
    # Verificar si el producto ya existe para actualizar
    for prod in inventario:
        if prod["nombre"].lower() == nombre_clean.lower():
            prod["cantidad"] += cantidad
            prod["precio"] = precio
            return

    # Si no existe, agregar nuevo producto
    inventario.append({"nombre": nombre_clean, "precio": float(precio), "cantidad": int(cantidad)})

def mostrar_inventario(inventario: List[Dict]) -> None:
    """
    Muestra todos los productos del inventario de forma ordenada.
    Parámetros:
    inventario (List[Dict]): lista de productos
    Retorno:
    None
    """

    if not inventario:
        print("\nEl inventario está vacío.")
        return

    print("\n---- Inventario ----")
    # Imprimir productos ordenados alfabéticamente

    for i, prod in enumerate(sorted(inventario, key=lambda p: p["nombre"].lower()), 1):
        print(f"{i}. {prod['nombre']} - Precio: {prod['precio']:.2f} - Cantidad: {prod['cantidad']}")
    print("--------------------")

def buscar_producto(inventario: List[Dict], nombre: str) -> Optional[Dict]:
    """
    Busca un producto por nombre en el inventario.
    Parámetros:
    inventario (List[Dict]): lista de productos
    nombre (str): nombre del producto a buscar
    Retorno:
    Dict del producto si se encuentra, None si no existe
    """

    nombre_clean = nombre.strip().lower()
    for prod in inventario:
        if prod["nombre"].lower() == nombre_clean:
            return prod
    return None

def actualizar_producto(inventario: List[Dict], nombre: str, nuevo_precio: Optional[float] = None,
                        nueva_cantidad: Optional[int] = None) -> bool:
    """
    Actualiza precio y/o cantidad de un producto existente.
    Parámetros:
    inventario (List[Dict]): lista de productos
    nombre (str): nombre del producto a actualizar
    nuevo_precio (float, opcional): nuevo precio
    nueva_cantidad (int, opcional): nueva cantidad
    Retorno:
    True si se actualizó correctamente, False si no se encontró el producto
    """

    prod = buscar_producto(inventario, nombre)
    if not prod:
        return False
    if nuevo_precio is not None:
        prod["precio"] = float(nuevo_precio)
    if nueva_cantidad is not None:
        prod["cantidad"] = int(nueva_cantidad)
    return True

def eliminar_producto(inventario: List[Dict], nombre: str) -> bool:
    """
    Elimina un producto del inventario por nombre.
    Parámetros:
    inventario (List[Dict]): lista de productos
    nombre (str): nombre del producto a eliminar
    Retorno:
    True si se eliminó, False si no se encontró
    """

    nombre_clean = nombre.strip().lower()
    for i, prod in enumerate(inventario):
        if prod["nombre"].lower() == nombre_clean:
            del inventario[i]
            return True
    return False

def calcular_estadisticas(inventario: List[Dict]) -> Dict:
    """
    Calcula estadísticas del inventario:
    - Unidades totales
    - Valor total
    - Producto más caro
    - Producto con mayor stock
    Parámetros:
    inventario (List[Dict]): lista de productos
    Retorno:
    Dict con estadísticas
    """

    if not inventario:
        return {
            "unidades_totales": 0,
            "valor_total": 0.0,
            "producto_mas_caro": None,
            "producto_mayor_stock": None
        }

    unidades_totales = sum(p["cantidad"] for p in inventario)
    # Calcular subtotal por producto usando lambda
    subtotal = lambda p: p["precio"] * p["cantidad"]
    valor_total = sum(subtotal(p) for p in inventario)

    # Identificar producto más caro y con mayor stock
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": {"nombre": producto_mas_caro["nombre"], "precio": producto_mas_caro["precio"]},
        "producto_mayor_stock": {"nombre": producto_mayor_stock["nombre"], "cantidad": producto_mayor_stock["cantidad"]}
    }