import json
import pandas as pd


niveles =  {
    'A' : 5,
    'B' : 10,
    'C' : 15,
    'CUAUH' : 20,
}


def leer_json(archivo):
    with open(archivo) as f:
        data = json.load(f)
        return data


def goles_por_nivel():
    """convertir el diccionario en un dataframe y crear una nueva columna (goles_por_nivel) que correlacione A,B,C o CUAUH con el número de goles"""
    data = leer_json('players.json')
    df = pd.DataFrame(data['jugadores'])

    # convertir valores de columna a mayúsculas para que concuerden con diccionario "levels"
    uppercased = df['nivel'].str.upper()

    # crear nueva columna con los goles que debe meter el jugador dependiendo su nivel
    df['goles_por_nivel'] = uppercased.map(niveles)
    return df

    """
    dataframe retornado
                   nombre  nivel  goles  sueldo   bono sueldo_completo  equipo  goles_por_nivel 
        0      Juan Perez      C     10   50000  25000            None   rojo               15               
        1        EL Cuauh  Cuauh     30  100000  30000            None   azul               20             
        2  Cosme Fulanito      A      7   20000  10000            None   azul                5                   
        3         El Rulo      B      9   30000  15000            None   rojo               10 
    """


def goles_por_equipo():
    """crear una nueva columna (total_goles_por_equipo) para sumar el total de goles por equipo"""
    data = goles_por_nivel()
    agrupado = data.groupby('equipo', as_index=False)['goles'].sum()
    columna_suma = agrupado['goles'].astype(str) + ' ' + agrupado['equipo']
    data['total_goles_por_equipo'] = columna_suma
    return data


    """
    dataframe retornado
                nombre  nivel  goles  sueldo  bono sueldo_completo equipo  goles_por_nivel total_goles_por_equipo
    0      Juan Perez      C     10   50000  25000            None   rojo               15                37 azul
    1        EL Cuauh  Cuauh     30  100000  30000            None   azul               20                19 rojo
    2  Cosme Fulanito      A      7   20000  10000            None   azul                5                    NaN
    3         El Rulo      B      9   30000  15000            None   rojo               10                    NaN
    """


def objetivo_goles_por_equipo():
    data = goles_por_equipo()
    agrupado = data.groupby('equipo', as_index=False)['goles_por_nivel'].sum()
    columna_suma = agrupado['goles_por_nivel'].astype(str) + ' ' + agrupado['equipo']
    data['objetivo_goles_por_equipo'] = columna_suma
    return data

    """
    dataframe retornado
           nombre  nivel  goles  sueldo   bono sueldo_completo  equipo  goles_por_nivel total_goles_por_equipo meta_goles_por_equipo
0      Juan Perez      C     10   50000  25000            None   rojo               15                37 azul               25 azul
1        EL Cuauh  Cuauh     30  100000  30000            None   azul               20                19 rojo               25 rojo
2  Cosme Fulanito      A      7   20000  10000            None   azul                5                    NaN                   NaN
3         El Rulo      B      9   30000  15000            None   rojo               10                    NaN                   NaN
    """


print(objetivo_goles_por_equipo())




# print(data.total_goles_por_equipo.str.split(' ').str[0])




