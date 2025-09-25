"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import pathlib

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    current_path = pathlib.Path(__file__).parent
    data_file = current_path.parent / "files/input/data.csv"

    with open(data_file, "r") as file:
        data = file.readlines()

    result = {}
    for line in data:
        parts = line.strip().split("\t")
        print(parts)
        letter = parts[0]
        number = int(parts[1])

        if letter not in result:
            result[letter] = [number, number]  # [max, min]
        else:
            if number > result[letter][0]:
                result[letter][0] = number
            if number < result[letter][1]:
                result[letter][1] = number

    final_result = [(key, value[0], value[1]) for key, value in sorted(result.items())]
    return final_result
