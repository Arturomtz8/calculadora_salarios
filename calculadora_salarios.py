import json
import numpy as np
import pandas as pd


niveles = {"A": 5, "B": 10, "C": 15, "CUAUH": 20}


class TableroJugadores:
    """
    para hacer una instancia de esta clase sólo requieres un
    parametro, el nombre del archivo. El método que se
    apoya en el resto de métodos es convertir_a_json.
    """
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def leer_json(self):
        with open(f"input_json/{self.nombre_archivo}") as f:
            data = json.load(f)
            return data

    def convertir_a_dataframe(self):
        """
        convierte el diccionario en un dataframe
        """
        data = self.leer_json()
        df = pd.DataFrame(data["jugadores"])
        return df

    def goles_mínimos(self):
        """
        sustituye la columna de "nivel" por el número de goles
        que debería meter cada jugador dependiendo su
        categoría y la renombra como "goles_mínimos".
        En caso de que la columna tenga el nivel como
        número, sólo renombrará la columna
        """
        df = self.convertir_a_dataframe()
        if not df["nivel"].dtype == np.int64:
            uppercased = df["nivel"].str.upper()
            df["nivel"] = uppercased.map(niveles)
        df.rename(columns={"nivel": "goles_mínimos"}, inplace=True)
        return df

        """
                   nombre  goles_mínimos  goles  sueldo   bono sueldo_completo equipo
        0      Juan Perez             15     10   50000  25000            None   rojo
        1        EL Cuauh             20     30  100000  30000            None   azul
        2  Cosme Fulanito              5      7   20000  10000            None   azul
        3         El Rulo             10      9   30000  15000            None   rojo
        """

    def porcentaje_goles_equipo(self):
        """
        calcula el porcentaje de goles por equipo, comparando el
        objetivo de goles vs los goles totales, que ayudará
        para deducir el 50% del bono de los jugadores
        """
        df = self.goles_mínimos()
        goles_equipo = df.groupby("equipo").agg({"goles": "sum"}) * 100
        objetivo_goles_equipo = df.groupby("equipo").agg({"goles_mínimos": "sum"})
        porcentaje_goles_equipo = goles_equipo.div(objetivo_goles_equipo.values).astype(float).round()
        porcentaje_goles_equipo.rename(columns={"goles": "porcentaje_goles_equipo"}, inplace=True)
        porcentaje_goles_equipo.reset_index(level=0, inplace=True)
        return porcentaje_goles_equipo

        """
          equipo  porcentaje_goles_equipo
        0   azul                    148.0
        1   rojo                     76.0
        """

    def porcentaje_goles_jugador(self):
        """
        deduce el otro 50% del bono de los jugadores. Compara el
        objetivo de goles de cada jugador dependiendo su
        nivel vs el total de goles individuales
        """
        df = self.goles_mínimos()
        total_goles = df.groupby("nombre").agg({"goles": "sum"}) * 100
        objetivo_goles_nivel = df.groupby("nombre").agg({"goles_mínimos": "sum"})
        porcentaje_goles_jugador = total_goles.div(objetivo_goles_nivel.values).astype(float).round()
        porcentaje_goles_jugador.rename(columns={"goles": "porcentaje_goles_jugador"}, inplace=True)
        porcentaje_goles_jugador.reset_index(level=0, inplace=True)
        return porcentaje_goles_jugador

        """
                   nombre   porcentaje_goles_jugador
        0  Cosme Fulanito                      140.0
        1        EL Cuauh                      150.0
        2         El Rulo                       90.0
        3      Juan Perez                       67.0
        """

    def unir_dataframe(self):
        """
        une tres dataframes: 1) el dataframe donde se renombra la columna
        "nivel" y se sustituyen las categorías por el mínimo de goles,
        2) el dataframe que contiene el porcentaje de goles por equipo
        y 3) el dataframe que tiene el porcentaje de goles por jugador
        """
        df_goles_mínimos = self.goles_mínimos()
        df_goles_equipo = self.porcentaje_goles_equipo()
        df_goles_jugador = self.porcentaje_goles_jugador()
        final_df = df_goles_mínimos.merge(df_goles_jugador, on="nombre").merge(df_goles_equipo, on="equipo")
        return final_df

        """
                   nombre  goles_mínimos  goles  sueldo   bono sueldo_completo  equipo  porcentaje_goles_jugador  porcentaje_goles_equipo
        0      Juan Perez             15     10   50000  25000            None   rojo                      67.0                     76.0
        1         El Rulo             10      9   30000  15000            None   rojo                      90.0                     76.0
        2        EL Cuauh             20     30  100000  30000            None   azul                     150.0                    148.0
        3  Cosme Fulanito              5      7   20000  10000            None   azul                     140.0                    148.0

        """

    def calcular_salario(self):
        """
        primero se obtiene el porcentaje del bono que le corresponde
        a cada jugador dependiendo del porcentaje de goles individuales
        y el porcentaje de goles de su equipo. Ese porcentaje ayuda
        para saber qué tanto del bono tendrá el jugador.
        Finalmente, el bono se suma al salario fijo
        """
        final_df = self.unir_dataframe()
        porcentaje_bono = (final_df["porcentaje_goles_equipo"] + final_df["porcentaje_goles_jugador"]) / 2
        bono = (porcentaje_bono * final_df["bono"]) / 100
        final_df["sueldo_completo"] = (final_df["sueldo"] + bono).astype(float).round(2)
        return final_df

        """
                    nombre  goles_mínimos  goles  sueldo  bono  sueldo_completo equipo  porcentaje_goles_jugador  porcentaje_goles_equipo
        0      Juan Perez             15     10   50000  25000          67875.0   rojo                      67.0                     76.0
        1         El Rulo             10      9   30000  15000          42450.0   rojo                      90.0                     76.0
        2        EL Cuauh             20     30  100000  30000         144700.0   azul                     150.0                    148.0
        3  Cosme Fulanito              5      7   20000  10000          34400.0   azul                     140.0                    148.0
        """

    def convertir_a_json(self):
        """
        guarda el dataframe en formato json. El archivo se
        guardará en la carpeta llamada "output" y su nombre
        será igual al nombre original del archivo más 'complete'
        para indicar que es el json con la columna del sueldo con valores
        """
        dicc_jugadores = dict()
        con_salario_df = self.calcular_salario()
        con_salario_df.drop(["porcentaje_goles_jugador", "porcentaje_goles_equipo"], axis=1, inplace=True)
        dicc_jugadores["jugadores"] = con_salario_df.to_dict("records")
        with open(f"output_json/{self.nombre_archivo}complete.json".replace(".json", "_", 1), "w") as f:
            json.dump(dicc_jugadores, f, indent=4, ensure_ascii=False)
        return dicc_jugadores
