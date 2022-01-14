from calculadora_salarios import TableroJugadores


tablero = TableroJugadores("más_equipos.json")
# print(tablero.goles_por_nivel())
print(tablero.porcentaje_goles_equipo())
print(tablero.porcentaje_goles_jugador())
# print(tablero.unir_dataframe())
# print(tablero.calcular_salario())
print(tablero.convertir_a_json())
