"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import pathlib

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    current_path = pathlib.Path(__file__).parent
    data_file = current_path.parent / "files/input/data.csv"

    with open(data_file, "r") as file:
        total = 0
        for line in file:
            total += int(line.split("\t")[1])
    return total
