def test_assert_simple():
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


def test_assert_teams():
    expected_json = {
    "jugadores" : [  
       {  
          "nombre":"Simón",
          "nivel":"C",
          "goles":13,
          "sueldo":70000,
          "bono":15000,
          "sueldo_completo":83050.0,
          "equipo":"verde"
       },
        {  
          "nombre":"Quique",
          "nivel":"Cuauh",
          "goles":5,
          "sueldo":60000,
          "bono":8000,
          "sueldo_completo":64480.0,
          "equipo":"verde"
 
       },
        {  
        "nombre":"Felipe",
        "nivel":"Cuauh",
        "goles":30,
        "sueldo":70000,
        "bono":25000,
        "sueldo_completo":99625.0,
        "equipo":"verde"

     },
       {  
          "nombre":"Alejandro",
          "nivel":"A",
          "goles":15,
          "sueldo":40000,
          "bono":10000,
          "sueldo_completo":57750.0,
          "equipo":"amarillo"
       },
        {  
        "nombre":"George",
        "nivel":"C",
        "goles":3,
        "sueldo":50000,
        "bono":5000,
        "sueldo_completo":51875.0,
        "equipo":"amarillo"

     },
    {  
        "nombre":"Gonzalo",
        "nivel":"Cuauh",
        "goles":4,
        "sueldo":60000,
        "bono":20000,
        "sueldo_completo":67500.0,
        "equipo":"amarillo"

     },

       {  
          "nombre":"Fernando",
          "nivel":"C",
          "goles":20,
          "sueldo":45000,
          "bono":13000,
          "sueldo_completo":63200.0,
          "equipo":"azul"
 
       },

     {  
        "nombre":"Rafa",
        "nivel":"A",
        "goles":16,
        "sueldo":20000,
        "bono":5000,
        "sueldo_completo":31675.0,
        "equipo":"azul"

     },

     {  
        "nombre":"Alberto",
        "nivel":"B",
        "goles":8,
        "sueldo":30000,
        "bono":2000,
        "sueldo_completo":32270.0,
        "equipo":"azul"

     },


    ]
 }
    return_json = {
    "jugadores": [
        {
            "nombre": "Simón",
            "nivel": "C",
            "goles": 13,
            "sueldo": 70000,
            "bono": 15000,
            "sueldo_completo": 83050.0,
            "equipo": "verde"
        },
        {
            "nombre": "Quique",
            "nivel": "Cuauh",
            "goles": 5,
            "sueldo": 60000,
            "bono": 8000,
            "sueldo_completo": 64480.0,
            "equipo": "verde"
        },
        {
            "nombre": "Felipe",
            "nivel": "Cuauh",
            "goles": 30,
            "sueldo": 70000,
            "bono": 25000,
            "sueldo_completo": 99625.0,
            "equipo": "verde"
        },
        {
            "nombre": "Alejandro",
            "nivel": "A",
            "goles": 15,
            "sueldo": 40000,
            "bono": 10000,
            "sueldo_completo": 57750.0,
            "equipo": "amarillo"
        },
        {
            "nombre": "George",
            "nivel": "C",
            "goles": 3,
            "sueldo": 50000,
            "bono": 5000,
            "sueldo_completo": 51875.0,
            "equipo": "amarillo"
        },
        {
            "nombre": "Gonzalo",
            "nivel": "Cuauh",
            "goles": 4,
            "sueldo": 60000,
            "bono": 20000,
            "sueldo_completo": 67500.0,
            "equipo": "amarillo"
        },
        {
            "nombre": "Fernando",
            "nivel": "C",
            "goles": 20,
            "sueldo": 45000,
            "bono": 13000,
            "sueldo_completo": 63200.0,
            "equipo": "azul"
        },
        {
            "nombre": "Rafa",
            "nivel": "A",
            "goles": 16,
            "sueldo": 20000,
            "bono": 5000,
            "sueldo_completo": 31675.0,
            "equipo": "azul"
        },
        {
            "nombre": "Alberto",
            "nivel": "B",
            "goles": 8,
            "sueldo": 30000,
            "bono": 2000,
            "sueldo_completo": 32270.0,
            "equipo": "azul"
        }
    ]
}
    assert  return_json == expected_json