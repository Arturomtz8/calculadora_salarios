import json
import pandas as pd
from functools import reduce


niveles =  {
    'A' : 5,
    'B' : 10,
    'C' : 15,
    'CUAUH' : 20,
}


class TableroJugadores:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    
    def leer_json(self):
        with open(self.nombre_archivo) as f:
            data = json.load(f)
            return data
    

    def convertir_a_dataframe(self):
        """convierte el diccionario en un dataframe"""
        data = self.leer_json()
        df = pd.DataFrame(data['jugadores'])
        return df


    def goles_por_nivel(self):
        """crea una nueva columna (goles_por_nivel) que correlacione A,B,C o CUAUH de cada jugador con el número de goles que deberían meter"""
        df = self.convertir_a_dataframe()
        # convertir valores de columna a mayúsculas para que concuerden con diccionario "levels"
        uppercased = df['nivel'].str.upper()
        # crear nueva columna con los goles que debe meter el jugador dependiendo su nivel
        df['goles_por_nivel'] = uppercased.map(niveles)
        return df

        """
                    nombre  nivel  goles  sueldo  bono sueldo_completo  equipo  goles_por_nivel 
        0      Juan Perez      C     10   50000  25000            None   rojo               15               
        1        EL Cuauh  Cuauh     30  100000  30000            None   azul               20             
        2  Cosme Fulanito      A      7   20000  10000            None   azul                5                   
        3         El Rulo      B      9   30000  15000            None   rojo               10 
        """


    def objetivo_goles_equipo(self):
        """calcular el objetivo de goles por equipo dependiendo del nivel de sus jugadores"""
        df = self.goles_por_nivel()
        objetivo_goles_equipo = df.groupby('equipo').agg({'goles_por_nivel': 'sum'})
        objetivo_goles_equipo.reset_index(level=0, inplace=True)
        objetivo_goles_equipo.rename(columns={'goles_por_nivel': 'objetivo_goles_equipo'}, inplace=True)
        return objetivo_goles_equipo
    
        """
          equipo  objetivo_goles_equipo
        0   azul                     25
        1   rojo                     25
        """


    def total_goles_equipo(self):
        """crea una nueva columna para sumar el total de goles por equipo"""
        df = self.convertir_a_dataframe()
        goles_equipo = df.groupby('equipo').agg({'goles': 'sum'})
        goles_equipo.reset_index(level=0, inplace=True)
        goles_equipo.rename(columns={'goles': 'total_goles_equipo'}, inplace=True)
        return goles_equipo

        """
          equipo  total_goles_equipo
        0   azul                  37
        1   rojo                  19
        """


    def porcentaje_goles_equipo(self):
        """calcula el porcentaje de goles por equipo que ayudará para deducir el 50% del bono de los jugadores"""
        df = self.goles_por_nivel()
        goles_equipo = df.groupby('equipo').agg({'goles': 'sum'}) * 100
        objetivo_goles_equipo = df.groupby('equipo').agg({'goles_por_nivel': 'sum'})
        porcentaje_goles_equipo = goles_equipo.div(objetivo_goles_equipo.values).astype(int)
        porcentaje_goles_equipo.rename(columns={'goles': 'porcentaje_goles_equipo'}, inplace=True)
        porcentaje_goles_equipo.reset_index(level=0, inplace=True)
        return porcentaje_goles_equipo

        """
          equipo  porcentaje_goles_equipo
        0   azul                      148
        1   rojo                       76
        """
        

    def porcentaje_goles_jugador(self):
        """calcula el porcentaje de goles por jugador para deducir el otro 50% del bono de los jugadores"""
        df = self.goles_por_nivel()
        total_goles = df.groupby('nombre').agg({'goles': 'sum'}) * 100
        objetivo_goles_nivel = df.groupby('nombre').agg({'goles_por_nivel': 'sum'})
        porcentaje_goles_jugador = total_goles.div(objetivo_goles_nivel.values).astype(float).round(1)
        porcentaje_goles_jugador.rename(columns={'goles': 'porcentaje_goles_jugador'}, inplace=True)
        porcentaje_goles_jugador.reset_index(level=0, inplace=True)
        return porcentaje_goles_jugador
        
        """
                   nombre  porcentaje_goles_jugador
        0  Cosme Fulanito                     140.0
        1        EL Cuauh                     150.0
        2         El Rulo                      90.0
        3      Juan Perez                      66.7
        """


    def unir_dataframe(self):
        df = self.goles_por_nivel()
        df2 = self.total_goles_equipo()
        df3 = self.objetivo_goles_equipo()
        df4 = self.porcentaje_goles_equipo()
        df5 = self.porcentaje_goles_jugador()
        dfs = [df, df2, df3, df4]
        df_con_cantidades_equipo = reduce(lambda left,right: pd.merge(left,right,on='equipo'), dfs)
        final_df = pd.merge(df_con_cantidades_equipo, df5)
        return final_df

        """
               nombre  nivel  goles  sueldo   bono sueldo_completo equipo  goles_por_nivel  total_goles_equipo  objetivo_goles_equipo  porcentaje_goles_equipo  porcentaje_goles_jugador
    0      Juan Perez      C     10   50000  25000            None   rojo               15                  19                     25                       76                      66.7
    1         El Rulo      B      9   30000  15000            None   rojo               10                  19                     25                       76                      90.0
    2        EL Cuauh  Cuauh     30  100000  30000            None   azul               20                  37                     25                      148                     150.0
    3  Cosme Fulanito      A      7   20000  10000            None   azul                5                  37                     25                      148                     140.0
        """
        

tablero = TableroJugadores('players.json')
print(tablero.objetivo_goles_equipo())
print(tablero.total_goles_equipo())
print(tablero.porcentaje_goles_equipo())
print(tablero.porcentaje_goles_jugador())
print(tablero.unir_dataframe())