"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import pathlib

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    current_path = pathlib.Path(__file__).parent
    data_file = current_path.parent / "files/input/data.csv"
    
    with open(data_file, "r") as file:
        sums = {}
        for line in file:
            parts = line.split("\t")
            letter = parts[0]
            number = int(parts[1])
            if letter in sums:
                sums[letter] += number
            else:
                sums[letter] = number

    return sorted(sums.items())
