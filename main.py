from calculadora_salarios import CalculadoraSalarios


calcular_tres_equipos = CalculadoraSalarios("más_equipos.json")
calcular_tres_equipos.convertir_a_json()

calcular_diff_nivel = CalculadoraSalarios("distintos_niveles.json", {"a": 10, "b": 20, "c": 30, "cuauh": 40})
calcular_diff_nivel.convertir_a_json()


calcular_diff_nivel_v2 = CalculadoraSalarios("distintos_niveles_vv2.json", {"a": 22, "b": 33, "c": 44, "cuauh": 55})
calcular_diff_nivel_v2.convertir_a_json()
