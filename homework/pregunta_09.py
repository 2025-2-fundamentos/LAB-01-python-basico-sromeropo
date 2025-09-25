"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import pathlib

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    current_path = pathlib.Path(__file__).parent
    data_file = current_path.parent / "files/input/data.csv"

    claves = {}
    with open(data_file, "r") as file:
        for line in file:
            campos = line.strip().split("\t")
            diccionario = campos[4].split(",")
            claves_vistas = set()
            for item in diccionario:
                clave, _ = item.split(":")
                if clave not in claves_vistas:
                    if clave not in claves:
                        claves[clave] = 1
                    else:
                        claves[clave] += 1
                    claves_vistas.add(clave)
    return dict(sorted(claves.items()))
