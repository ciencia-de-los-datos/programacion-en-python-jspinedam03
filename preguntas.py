"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open('data.csv', 'r') as f:
        suma_segunda_colm = 0
        for row in f:
            row = row.split("\t")
            suma_segunda_colm = suma_segunda_colm + float(row[1]) 
            
            
    return suma_segunda_colm


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open('data.csv', 'r') as archivo_csv:
    # Lee todas las líneas del archivo
        lineas = archivo_csv.readlines()
        lineas.count

    for linea in lineas:
        valores = linea.strip()

        #print(valores)


    dic = []
    suma_a = 0  
    suma_b = 0  
    suma_c = 0  
    suma_d = 0 
    suma_e = 0
    for fila in lineas:
        if fila[0] == "A":
            suma_a = suma_a + 1
        if fila[0] == "B":
            suma_b = suma_b + 1
        if fila[0] == "C":
            suma_c = suma_c + 1
        if fila[0] == "D":
            suma_d = suma_d + 1
        if fila[0] == "E":
            suma_e = suma_e + 1
    dic = [("A", suma_a), ("B", suma_b),("C", suma_c),("D", suma_d),("E", suma_e)] 

    return dic


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open('data.csv', 'r') as f:
        
        
    
        f = [x.replace("\n", "") for x in f ]
        f = [y.split("\t") for y in f ]

        ext_letras = [t[0][0] for t in f]
        numeros = [int(t[1]) for t in f]


        sum_ext_letras = {}

        for letra, valor in zip(ext_letras, numeros):
            if letra in sum_ext_letras:
                sum_ext_letras[letra] += valor
            else:
                sum_ext_letras[letra] = valor

        resultado = sorted([(letra, suma) for letra, suma in sum_ext_letras.items()])
        
    return resultado


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open('data.csv', 'r') as f:
        
        f = [x.replace("\n", "") for x in f ]
        f = [y.split("\t") for y in f ]
    
    

        fecha_mes = [t[2].split("-")[1] for t in f]
        fecha_mes

        result = [(mes, fecha_mes.count(mes)) for mes in sorted(set(fecha_mes))]

    return result


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open('data.csv', 'r') as f:


        f = [x.replace("\n", "") for x in f ]
        f = [y.split("\t") for y in f ]

        letras = [t[0][0] for t in f]
        numeros = [int(t[1][0]) for t in f]
        lista = list(zip(letras, numeros))

        maximos_minimos = {}

        for letra, valor in lista:
            if letra not in maximos_minimos:
                maximos_minimos[letra] = {"maximo": valor, "minimo": valor}
            else:
                if valor > maximos_minimos[letra]["maximo"]:
                    maximos_minimos[letra]["maximo"] = valor
                if valor < maximos_minimos[letra]["minimo"]:
                    maximos_minimos[letra]["minimo"] = valor

        resultado = [(letra, maximos_minimos[letra]["maximo"], maximos_minimos[letra]["minimo"]) for letra in maximos_minimos]
        resultado = sorted(resultado, key=lambda resultado: resultado[0])

        
        return resultado


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open('data.csv', 'r') as f:


        f = [x.replace("\n", "") for x in f ]
        f = [y.split("\t") for y in f ]
        
        min_max_dict = {}

        for fila in f:
            col5_dict = fila[4]
            for llave_numero in col5_dict.split(","):
                llave, numero = llave_numero.split(":")
                numero = int(numero)
                if llave in min_max_dict:

                    min_max_dict[llave].append(numero)
                else:
                    min_max_dict[llave] = [numero]
            min_max_dict
            resultado = []
            for llave, numeros in sorted((min_max_dict.items())):
                resultado.append((llave, min(numeros), max(numeros)))

        
    return resultado


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open('data.csv', 'r') as f:
        f = [row_1.replace("\n", "") for row_1 in f ]
        f = [row_1.split("\t") for row_1 in f ]




        resultado = []
        lista_letra_numero = [(int(t[1]), t[0]) for t in f]

        for extrac_numero in sorted(set(t[0] for t in lista_letra_numero)):

            letras = [t[1] for t in lista_letra_numero if t[0] == extrac_numero]
            resultado.append((extrac_numero, letras))


        resultado = sorted(resultado, key=lambda x: x[0])
 
    return resultado


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open('data.csv', 'r') as f:
        f = [row_1.replace("\n", "") for row_1 in f ]
        f = [row_1.split("\t") for row_1 in f ]




        resultado = []
        lista_letra_numero = [(int(t[1]), t[0]) for t in f]

        for extrac_numero in sorted(set(t[0] for t in lista_letra_numero)):

            letras = sorted(set([t[1] for t in lista_letra_numero if t[0] == extrac_numero]))
            resultado.append((extrac_numero, letras))


        resultado = sorted(resultado, key=lambda x: x[0])

    return resultado


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open('data.csv', 'r') as f:
        dicc_letras_valores = {}
        f = [x.replace("\n", "") for x in f ]
        f = [y.split("\t") for y in f ]

        for row in f:
            columna5_dic = row[4]
            for key_valor in columna5_dic.split(","):
                key, valor = key_valor.split(":")
                valor = int(valor)
                if key in dicc_letras_valores:
                    dicc_letras_valores[key].append(valor)
                else:
                    dicc_letras_valores[key] = [valor]
                    



        resultado = { key:len(valores) for key, valores in sorted(dicc_letras_valores.items()) }
    
    return resultado


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open('data.csv', 'r') as f:
        f = [x.replace("\n", "") for x in f ]
        f = [y.split("\t") for y in f ]

        columna0 = [t[0] for t in f]
        calomna4 =[len(t[3].split(',')) for t in f]
        columna5 =[len((t[4]).split(',')) for t in f]
        
        resultado = list(zip(columna0,calomna4, columna5))
        
    return resultado


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open('data.csv', 'r') as f:
        
        f = [x.replace("\n", "") for x in f ]
        f = [y.split("\t") for y in f ]

        columna2 = [int(t[1]) for t in f]
        columna4 = [t[3] for t in f]

        resultado_dicc = {}

        for i in range(len(columna2)):
            keys = columna4[i].split(",")
            for key in keys:
                if key in resultado_dicc:
                    resultado_dicc[key] += columna2[i]
                else:
                    resultado_dicc[key] = columna2[i]

        sorted_dict = dict(sorted(resultado_dicc.items()))

        format_dicc = {}
        for key, value in sorted_dict.items():
            format_dicc[key] = value
            
            
        return format_dicc
   


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open('data.csv', 'r') as f:

        resultado = {}

        for line in f:
            elementos = line.strip().split('\t')
            column1, column5 = elementos[0], elementos[4]
            total = 0
            for pair in column5.split(','):
                total += int(pair.split(':')[1])
            if column1 in resultado:
                resultado[column1] += total
            else:
                resultado[column1] = total

        resultado = dict(sorted(resultado.items()))


        return resultado
