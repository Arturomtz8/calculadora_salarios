def test_assert_equal():
    expected_json = {
    "jugadores" : [  
       {  
          "nombre":"Juan",
          "nivel":"A",
          "goles":6,
          "sueldo":50000,
          "bono":25000,
          "sueldo_completo":77000.0,
          "equipo":"rojo"
       },
       {  
          "nombre":"Pedro",
          "nivel":"B",
          "goles":7,
          "sueldo":100000,
          "bono":30000,
          "sueldo_completo":124900.0,
          "equipo":"rojo"
       },
       {  
          "nombre":"Martín",
          "nivel":"C",
          "goles":16,
          "sueldo":20000,
          "bono":10000,
          "sueldo_completo":30133.5,
          "equipo":"rojo"
 
       },
       {  
          "nombre":"Luis",
          "nivel":"Cuauh",
          "goles":19,
          "sueldo":50000,
          "bono":10000,
          "sueldo_completo":59550.0,
          "equipo":"rojo"
 
       }
    ]
 }
    return_json = {
    "jugadores": [
        {
            "nombre": "Juan",
            "nivel": "A",
            "goles": 6,
            "sueldo": 50000,
            "bono": 25000,
            "sueldo_completo": 77000.0,
            "equipo": "rojo"
        },
        {
            "nombre": "Pedro",
            "nivel": "B",
            "goles": 7,
            "sueldo": 100000,
            "bono": 30000,
            "sueldo_completo": 124900.0,
            "equipo": "rojo"
        },
        {
            "nombre": "Martín",
            "nivel": "C",
            "goles": 16,
            "sueldo": 20000,
            "bono": 10000,
            "sueldo_completo": 30133.5,
            "equipo": "rojo"
        },
        {
            "nombre": "Luis",
            "nivel": "Cuauh",
            "goles": 19,
            "sueldo": 50000,
            "bono": 10000,
            "sueldo_completo": 59550.0,
            "equipo": "rojo"
        }
    ]
}
    assert  return_json == expected_json