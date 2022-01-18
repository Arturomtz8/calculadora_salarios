import json


def abrir_json(nombre_archivo):
    with open(f"output_json/{nombre_archivo}") as f:
        my_json = json.load(f)
        return my_json


def test_assert_simple():
    expected_json = {
        "jugadores": [
            {
                "nombre": "Juan",
                "goles_mínimos": 5,
                "goles": 6,
                "sueldo": 50000,
                "bono": 25000,
                "sueldo_completo": 77000.0,
                "equipo": "rojo",
            },
            {
                "nombre": "Pedro",
                "goles_mínimos": 10,
                "goles": 7,
                "sueldo": 100_000,
                "bono": 30000,
                "sueldo_completo": 124_900.0,
                "equipo": "rojo",
            },
            {
                "nombre": "Martín",
                "goles_mínimos": 15,
                "goles": 16,
                "sueldo": 20000,
                "bono": 10000,
                "sueldo_completo": 30150.0,
                "equipo": "rojo",
            },
            {
                "nombre": "Luis",
                "goles_mínimos": 20,
                "goles": 19,
                "sueldo": 50000,
                "bono": 10000,
                "sueldo_completo": 59550.0,
                "equipo": "rojo",
            },
        ]
    }
    return_json = abrir_json("primera_prueba_complete.json")

    assert return_json == expected_json


def test_assert_equipos():
    expected_json = {
        "jugadores": [
            {
                "nombre": "Simón",
                "goles_mínimos": 15,
                "goles": 13,
                "sueldo": 70000,
                "bono": 15000,
                "sueldo_completo": 83050.0,
                "equipo": "verde",
            },
            {
                "nombre": "Quique",
                "goles_mínimos": 20,
                "goles": 5,
                "sueldo": 60000,
                "bono": 8000,
                "sueldo_completo": 64480.0,
                "equipo": "verde",
            },
            {
                "nombre": "Felipe",
                "goles_mínimos": 20,
                "goles": 30,
                "sueldo": 70000,
                "bono": 25000,
                "sueldo_completo": 99625.0,
                "equipo": "verde",
            },
            {
                "nombre": "Alejandro",
                "goles_mínimos": 5,
                "goles": 15,
                "sueldo": 40000,
                "bono": 10000,
                "sueldo_completo": 57750.0,
                "equipo": "amarillo",
            },
            {
                "nombre": "George",
                "goles_mínimos": 15,
                "goles": 3,
                "sueldo": 50000,
                "bono": 5000,
                "sueldo_completo": 51875.0,
                "equipo": "amarillo",
            },
            {
                "nombre": "Gonzalo",
                "goles_mínimos": 20,
                "goles": 4,
                "sueldo": 60000,
                "bono": 20000,
                "sueldo_completo": 67500.0,
                "equipo": "amarillo",
            },
            {
                "nombre": "Fernando",
                "goles_mínimos": 15,
                "goles": 20,
                "sueldo": 45000,
                "bono": 13000,
                "sueldo_completo": 63200.0,
                "equipo": "azul",
            },
            {
                "nombre": "Rafa",
                "goles_mínimos": 5,
                "goles": 16,
                "sueldo": 20000,
                "bono": 5000,
                "sueldo_completo": 31675.0,
                "equipo": "azul",
            },
            {
                "nombre": "Alberto",
                "goles_mínimos": 10,
                "goles": 8,
                "sueldo": 30000,
                "bono": 2000,
                "sueldo_completo": 32270.0,
                "equipo": "azul",
            },
        ]
    }

    return_json = abrir_json("más_equipos_complete.json")

    assert return_json == expected_json


def test_assert_diferentes_niveles():
    expected_json = {
        "jugadores": [
            {
                "nombre": "Roberto",
                "goles_mínimos": 10,
                "goles": 24,
                "sueldo": 40000,
                "bono": 13000,
                "sueldo_completo": 62165.0,
                "equipo": "azul",
            },
            {
                "nombre": "Fernando",
                "goles_mínimos": 40,
                "goles": 38,
                "sueldo": 45000,
                "bono": 28000,
                "sueldo_completo": 72440.0,
                "equipo": "azul",
            },
            {
                "nombre": "Esteban",
                "goles_mínimos": 30,
                "goles": 21,
                "sueldo": 40000,
                "bono": 24000,
                "sueldo_completo": 60520.0,
                "equipo": "azul",
            },
            {
                "nombre": "José Luis",
                "goles_mínimos": 20,
                "goles": 18,
                "sueldo": 28000,
                "bono": 8000,
                "sueldo_completo": 35640.0,
                "equipo": "azul",
            },
        ]
    }

    return_json = abrir_json("distintos_niveles_complete.json")

    assert return_json == expected_json


def test_assert_más_equipos_niveles():
    expected_json = {
        "jugadores": [
            {
                "nombre": "Antonio",
                "goles_mínimos": 55,
                "goles": 27,
                "sueldo": 35000,
                "bono": 8000,
                "sueldo_completo": 39760.0,
                "equipo": "morado",
            },
            {
                "nombre": "David",
                "goles_mínimos": 33,
                "goles": 24,
                "sueldo": 36000,
                "bono": 5500,
                "sueldo_completo": 39932.5,
                "equipo": "morado",
            },
            {
                "nombre": "Joel",
                "goles_mínimos": 22,
                "goles": 30,
                "sueldo": 26000,
                "bono": 9000,
                "sueldo_completo": 35270.0,
                "equipo": "morado",
            },
            {
                "nombre": "Edwin",
                "goles_mínimos": 55,
                "goles": 35,
                "sueldo": 60000,
                "bono": 15000,
                "sueldo_completo": 70050.0,
                "equipo": "morado",
            },
            {
                "nombre": "Fernando",
                "goles_mínimos": 44,
                "goles": 40,
                "sueldo": 44000,
                "bono": 6400,
                "sueldo_completo": 48768.0,
                "equipo": "verde",
            },
            {
                "nombre": "Enrique",
                "goles_mínimos": 22,
                "goles": 9,
                "sueldo": 25000,
                "bono": 7000,
                "sueldo_completo": 28465.0,
                "equipo": "verde",
            },
            {
                "nombre": "Homero",
                "goles_mínimos": 33,
                "goles": 19,
                "sueldo": 40000,
                "bono": 18000,
                "sueldo_completo": 50440.0,
                "equipo": "verde",
            },
            {
                "nombre": "Ariel",
                "goles_mínimos": 33,
                "goles": 9,
                "sueldo": 20000,
                "bono": 5000,
                "sueldo_completo": 22125.0,
                "equipo": "verde",
            },
            {
                "nombre": "Mario",
                "goles_mínimos": 22,
                "goles": 33,
                "sueldo": 25000,
                "bono": 2300,
                "sueldo_completo": 27932.5,
                "equipo": "azul",
            },
            {
                "nombre": "John",
                "goles_mínimos": 44,
                "goles": 41,
                "sueldo": 60000,
                "bono": 10000,
                "sueldo_completo": 69900.0,
                "equipo": "azul",
            },
            {
                "nombre": "Juan Pablo",
                "goles_mínimos": 55,
                "goles": 33,
                "sueldo": 65000,
                "bono": 20000,
                "sueldo_completo": 81500.0,
                "equipo": "azul",
            },
            {
                "nombre": "Daniel",
                "goles_mínimos": 44,
                "goles": 67,
                "sueldo": 75000,
                "bono": 30000,
                "sueldo_completo": 113_550.0,
                "equipo": "azul",
            },
        ]
    }

    return_json = abrir_json("distintos_niveles_vv2_complete.json")

    assert return_json == expected_json
