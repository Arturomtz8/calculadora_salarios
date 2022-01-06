import json
import pandas as pd


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


    def total_goles_equipo(self):
        """crea una nueva columna para sumar el total de goles por equipo"""
        df = self.convertir_a_dataframe()
        agrupado = df.groupby('equipo', as_index=False)['goles'].sum()
        columna_suma = agrupado['goles'].astype(str) + ' ' + agrupado['equipo']
        return columna_suma

        """
        0    37 azul
        1    19 rojo
        dtype: object
        """


    def objetivo_goles_equipo(self):
        """crea un data frame donde suma, basado en el nivel de cada jugador, el objetivo deseado de goles por equipo"""
        df = self.goles_por_nivel()
        agrupado = df.groupby('equipo', as_index=False)['goles_por_nivel'].sum()
        columna_suma = agrupado['goles_por_nivel'].astype(str) + ' ' + agrupado['equipo']
        df['objetivo_goles_equipo'] = columna_suma
        return df

        """
                   nombre  nivel  goles  sueldo   bono sueldo_completo equipo  goles_por_nivel    objetivo_goles_equipo
        0      Juan Perez      C     10   50000  25000            None   rojo               15                   25 azul
        1        EL Cuauh  Cuauh     30  100000  30000            None   azul               20                   25 rojo
        2  Cosme Fulanito      A      7   20000  10000            None   azul                5                       NaN
        3         El Rulo      B      9   30000  15000            None   rojo               10                       NaN
        """
    

    def unir_dataframe(self):
        """une la columna de los goles anotados realmente por el equipo con las columnas "goles_por_nivel" y "objetivo_goles_equipo" """
        df = self.objetivo_goles_equipo()
        df['total_goles_equipo'] = self.total_goles_equipo()
        return df

        """
                   nombre  nivel  goles  sueldo   bono sueldo_completo equipo  goles_por_nivel objetivo_goles_equipo total_goles_equipo
        0      Juan Perez      C     10   50000  25000            None   rojo               15               25 azul            37 azul
        1        EL Cuauh  Cuauh     30  100000  30000            None   azul               20               25 rojo            19 rojo
        2  Cosme Fulanito      A      7   20000  10000            None   azul                5                   NaN                NaN
        3         El Rulo      B      9   30000  15000            None   rojo               10                   NaN                NaN
        """



tablero = TableroJugadores('players.json')
print(tablero.unir_dataframe())




# print(data.total_total_goles_por_equipo.str.split(' ').str[0])




