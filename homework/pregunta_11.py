"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import pathlib

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    current_path = pathlib.Path(__file__).parent
    data_file = current_path.parent / "files/input/data.csv"
    suma_col2 = {}
    with open(data_file, "r") as file:
        for line in file:
            campos = line.strip().split("\t")
            valor_col2 = int(campos[1])
            letras_col4 = campos[3].split(",")
            for letra in letras_col4:
                if letra not in suma_col2:
                    suma_col2[letra] = valor_col2
                else:
                    suma_col2[letra] += valor_col2
    return dict(sorted(suma_col2.items()))
