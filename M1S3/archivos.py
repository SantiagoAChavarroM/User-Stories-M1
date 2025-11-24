# -----------------------------------------------------------
# Funciones para guardar y cargar inventarios en formato CSV.
# -----------------------------------------------------------

import csv
from typing import List, Dict, Tuple

def guardar_csv(inventario: List[Dict], ruta: str, incluir_header: bool = True) -> bool:
    """
    Guarda el inventario en un archivo CSV.

    Parámetros:
    inventario (List[Dict]): lista de productos
    ruta (str): ruta del archivo CSV destino
    incluir_header (bool): si se incluye encabezado en CSV (default True)

    Retorno:
    True si se guardó correctamente, False si hubo error o inventario vacío
    """
    if not inventario:
        print("No se puede guardar: el inventario está vacío.")
        return False

    try:
        with open(ruta, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            # Escribir encabezado si corresponde
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])
            # Escribir productos
            for p in inventario:
                writer.writerow([p["nombre"], f"{p['precio']:.2f}", p["cantidad"]])
        print(f"Inventario guardado en: {ruta}")
        return True
    except PermissionError:
        print("Error: permiso denegado al intentar escribir el archivo. Verifica permisos o ruta.")
        return False
    except OSError as e:
        print(f"Error de E/S al guardar el archivo: {e}")
        return False
    except Exception as e:
        print(f"Error inesperado al guardar: {e}")
        return False


def cargar_csv(ruta: str) -> Tuple[List[Dict], int]:
    """
    Carga productos desde un archivo CSV al inventario.

    Parámetros:
    ruta (str): ruta del archivo CSV a leer

    Retorno:
    Tuple[List[Dict], int]: lista de productos cargados y número de filas inválidas
    """
    productos = []
    filas_invalidas = 0
    try:
        with open(ruta, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            try:
                header = next(reader)
            except StopIteration:
                print("El archivo CSV está vacío.")
                return [], 0

            # Validar encabezado
            expected_header = ["nombre", "precio", "cantidad"]
            if [h.strip().lower() for h in header] != expected_header:
                print(f"Encabezado inválido. Se esperaba: {','.join(expected_header)}. Encontrado: {','.join(header)}")
                return [], 0

            # Leer filas de productos
            for i, row in enumerate(reader, start=2):
                if len(row) != 3:
                    filas_invalidas += 1
                    continue
                nombre, precio_s, cantidad_s = row
                try:
                    precio = float(precio_s)
                    cantidad = int(float(cantidad_s))
                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue
                    # Agregar producto válido
                    productos.append({"nombre": nombre.strip(), "precio": precio, "cantidad": cantidad})
                except ValueError:
                    filas_invalidas += 1
                    continue
        return productos, filas_invalidas
    except FileNotFoundError:
        print("Error: archivo no encontrado.")
        return [], 0
    except UnicodeDecodeError:
        print("Error: problema de codificación al leer el archivo. Intenta de nuevo.")
        return [], 0
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
        return [], 0