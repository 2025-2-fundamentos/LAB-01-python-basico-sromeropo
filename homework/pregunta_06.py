"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import pathlib

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    current_path = pathlib.Path(__file__).parent
    data_file = current_path.parent / "files/input/data.csv"

    claves = {}
    with open(data_file, "r") as file:
        for line in file:
            campos = line.strip().split("\t")
            diccionario = campos[4].split(",")
            for item in diccionario:
                clave, valor = item.split(":")
                valor = int(valor)
                if clave not in claves:
                    claves[clave] = [valor, valor]
                else:
                    if valor < claves[clave][0]:
                        claves[clave][0] = valor
                    if valor > claves[clave][1]:
                        claves[clave][1] = valor
    resultado = [(clave, min_max[0], min_max[1]) for clave, min_max in sorted(claves.items())]
    return resultado
