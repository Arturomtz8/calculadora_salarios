from calculadora_salarios import CalculadoraSalarios


equipo_rojo = CalculadoraSalarios("ejemplo_repo.json")
equipo_rojo.convertir_a_json()

calcular_un_equipo = CalculadoraSalarios("un_equipo.json")
calcular_un_equipo.convertir_a_json()

calcular_dos_equipos = CalculadoraSalarios("repo_dos_equipos.json")
calcular_dos_equipos.convertir_a_json()

calcular_tres_equipos = CalculadoraSalarios("tres_equipos.json")
calcular_tres_equipos.convertir_a_json()

calcular_dif_nivel = CalculadoraSalarios("distintos_niveles.json", {"a": 10, "b": 20, "c": 30, "cuauh": 40})
calcular_dif_nivel.convertir_a_json()

calcular_dif_nivel_v2 = CalculadoraSalarios("distintos_niveles_vv2.json", {"a": 22, "b": 33, "c": 44, "cuauh": 55})
calcular_dif_nivel_v2.convertir_a_json()
