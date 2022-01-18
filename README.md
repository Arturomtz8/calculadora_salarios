# Solución al problema de [los salarios de los jugadores](https://github.com/resuelve/prueba-ing-backend).

Este proyecto usa `pandas`, si no lo tienes instalado, ejecuta:

```shell
$ pip install pandas
```

En el archivo `main.py` se importa la clase `CalculadoraSalarios` creada en el archivo `calculadora_salarios.py`. La función de esta clase está en su nombre, en base al porcentaje del bono dependiendo de su desempeño tanto individual como de equipo, obtiene el salario final de cada jugador. Para iniciar una instancia de esta clase, el único argumento obligatorio es el nombre del archivo `json`, donde se encuentra la información de los jugadores. Para mantener en orden el código, la clase `CalculadoraSalarios` busca los archivos `json` en la carpeta  `input_json`, así que si quieres probar con otro archivo, tendrás que guardar el `json` en dicha carpeta.
Ejemplo de instanciar una clase:

```python
from calculadora_salarios import CalculadoraSalarios


calcular_tres_equipos = CalculadoraSalarios("tres_equipos.json")
```

El método `.convertir_a_json()` calculará el salario y guardará los resultados en la carpeta `output_json`:

```python
from calculadora_salarios import CalculadoraSalarios


calcular_tres_equipos = CalculadoraSalarios("tres_equipos.json")
calcular_tres_equipos.convertir_a_json()
```

Ejemplo de json guardado en carpeta `output_json` con el campo "sueldo_completo" con el monto correcto:
```json
{
    "jugadores": [
        {
            "nombre": "Juan",
            "goles_mínimos": 5,
            "goles": 6,
            "sueldo": 50000,
            "bono": 25000,
            "sueldo_completo": 77000.0,
            "equipo": "rojo"
        },
        {
            "nombre": "Pedro",
            "goles_mínimos": 10,
            "goles": 7,
            "sueldo": 100000,
            "bono": 30000,
            "sueldo_completo": 124900.0,
            "equipo": "rojo"
        },
        {
            "nombre": "Martín",
            "goles_mínimos": 15,
            "goles": 16,
            "sueldo": 20000,
            "bono": 10000,
            "sueldo_completo": 30150.0,
            "equipo": "rojo"
        },
        {
            "nombre": "Luis",
            "goles_mínimos": 20,
            "goles": 19,
            "sueldo": 50000,
            "bono": 10000,
            "sueldo_completo": 59550.0,
            "equipo": "rojo"
        }
    ]
}
```

Si quieres ingresar distintos niveles de los jugadores, puedes ingresar como segundo argumento de la clase `CalculadoraSalarios` los nuevos niveles en forma de diccionario:

```python
from calculadora_salarios import CalculadoraSalarios


calcular_dif_nivel = CalculadoraSalarios("distintos_niveles.json", {"a": 10, "b": 20, "c": 30, "cuauh": 40})
calcular_dif_nivel.convertir_a_json()
```