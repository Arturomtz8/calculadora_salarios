import json
import pandas as pd


niveles = {"A": 5, "B": 10, "C": 15, "CUAUH": 20}


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
        df = pd.DataFrame(data["jugadores"])
        return df

    def goles_por_nivel(self):
        """crea una nueva columna (goles_por_nivel) que correlacione A,B,C o CUAUH de cada 
        jugador con el número de goles que deberían meter"""
        df = self.convertir_a_dataframe()
        # convertir valores de columna a mayúsculas para que concuerden con diccionario "levels"
        uppercased = df["nivel"].str.upper()
        # crear nueva columna con los goles que debe meter el jugador dependiendo su nivel
        df["goles_por_nivel"] = uppercased.map(niveles)
        return df

        """
                   nombre  nivel  goles  sueldo   bono sueldo_completo equipo  goles_por_nivel
        0      Juan Perez      C     10   50000  25000            None   rojo               15
        1        EL Cuauh  Cuauh     30  100000  30000            None   azul               20
        2  Cosme Fulanito      A      7   20000  10000            None   azul                5
        3         El Rulo      B      9   30000  15000            None   rojo               10
        """

    def porcentaje_goles_equipo(self):
        """calcula el porcentaje de goles por equipo, comparando el objetivo de goles vs los goles 
        totales, que ayudará para deducir el 50% del bono de los jugadores"""
        df = self.goles_por_nivel()
        goles_equipo = df.groupby("equipo").agg({"goles": "sum"}) * 100
        objetivo_goles_equipo = df.groupby("equipo").agg({"goles_por_nivel": "sum"})
        porcentaje_goles_equipo = goles_equipo.div(objetivo_goles_equipo.values).astype(int)
        porcentaje_goles_equipo.rename(columns={"goles": "porcentaje_goles_equipo"}, inplace=True)
        porcentaje_goles_equipo.reset_index(level=0, inplace=True)
        return porcentaje_goles_equipo

        """
          equipo  porcentaje_goles_equipo
        0   azul                      148
        1   rojo                       76
        """

    def porcentaje_goles_jugador(self):
        """deduce el otro 50% del bono de los jugadores. Compara el objetivo de goles de cada 
        jugador dependiendo su nivel vs el total de goles individuales"""
        df = self.goles_por_nivel()
        total_goles = df.groupby("nombre").agg({"goles": "sum"}) * 100
        objetivo_goles_nivel = df.groupby("nombre").agg({"goles_por_nivel": "sum"})
        porcentaje_goles_jugador = total_goles.div(objetivo_goles_nivel.values).astype(float).round(2)
        porcentaje_goles_jugador.rename(columns={"goles": "porcentaje_goles_jugador"}, inplace=True)
        porcentaje_goles_jugador.reset_index(level=0, inplace=True)
        return porcentaje_goles_jugador

        """
                   nombre   porcentaje_goles_jugador
        0  Cosme Fulanito                     140.00
        1        EL Cuauh                     150.00
        2         El Rulo                      90.00
        3      Juan Perez                      66.67
        """

    def unir_dataframe(self):
        """une tres dataframes: 1) el primero sacado del json, 2) el dataframe que contiene 
        el porcentaje de goles por equipo y 3) el dataframe que tiene el porcentaje de goles por jugador"""
        df_inicial = self.convertir_a_dataframe()
        df_goles_equipo = self.porcentaje_goles_equipo()
        df_goles_jugador = self.porcentaje_goles_jugador()
        final_df = df_inicial.merge(df_goles_jugador, on="nombre").merge(df_goles_equipo, on="equipo")
        return final_df

        """
                   nombre  nivel  goles  sueldo   bono sueldo_completo equipo  porcentaje_goles_jugador  porcentaje_goles_equipo
        0      Juan Perez      C     10   50000  25000            None   rojo                     66.67                       76
        1         El Rulo      B      9   30000  15000            None   rojo                     90.00                       76
        2        EL Cuauh  Cuauh     30  100000  30000            None   azul                    150.00                      148
        3  Cosme Fulanito      A      7   20000  10000            None   azul                    140.00                      148

        """

    def calcular_salario(self):
        """primero se obtiene el porcentaje del bono que le corresponde a cada jugador dependiendo 
        del porcentaje de goles individuales y el porcentaje de goles de su equipo. Ese porcentaje 
        ayuda para saber qué tanto del bono tendrá el jugador. Finalmente, el bono se suma al salario fijo"""
        final_df = self.unir_dataframe()
        porcentaje_bono = (final_df["porcentaje_goles_equipo"] + final_df["porcentaje_goles_jugador"]) / 2
        bono = (porcentaje_bono * final_df["bono"]) / 100
        final_df["sueldo_completo"] = (final_df["sueldo"] + bono).astype(float).round(2)
        return final_df

        """
                   nombre  nivel  goles  sueldo   bono  sueldo_completo equipo   porcentaje_goles_jugador  porcentaje_goles_equipo
        0      Juan Perez      C     10   50000  25000         67833.75   rojo                     66.67                       76
        1         El Rulo      B      9   30000  15000         42450.00   rojo                     90.00                       76
        2        EL Cuauh  Cuauh     30  100000  30000        144700.00   azul                    150.00                      148
        3  Cosme Fulanito      A      7   20000  10000         34400.00   azul                    140.00                      148
        """

    def convertir_a_json(self):
        """guarda el dataframe en formato json. El archivo se guardará en la misma carpeta donde 
        se ejecute el programa y su nombre será igual al nombre original del archivo más 'output' para 
        indicar que es el json con la columna del sueldo con valores"""
        dicc_jugadores = dict()
        con_salario_df = self.calcular_salario()
        con_salario_df.drop(["porcentaje_goles_jugador", "porcentaje_goles_equipo"], axis=1, inplace=True)
        dicc_jugadores["jugadores"] = con_salario_df.to_dict("records")
        with open(f"{self.nombre_archivo}output.json".replace(".json", "_", 1), "w") as f:
            json.dump(dicc_jugadores, f, indent=4)
        return dicc_jugadores


tablero = TableroJugadores("primera_prueba.json")
# print(tablero.goles_por_nivel())
# print(tablero.porcentaje_goles_equipo())
# print(tablero.porcentaje_goles_jugador())
# print(tablero.unir_dataframe())
# print(tablero.calcular_salario())
print(tablero.convertir_a_json())
