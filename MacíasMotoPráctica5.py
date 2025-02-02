# -*- coding: utf-8 -*-
"""Practica5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-OV4BMOyOwsYTeTTChM19x3XVh2XKu35

Equipo

1. Nathalia Jazmin Ballesteros Luna
2. Luis Armando Macias Moto

# EJERCICIO 1
"""

import numpy as np
import matplotlib.pyplot as plt

#Definimos la función recursiva para Pn+1 = aPn + b
def sistema_dinamico(a, b, P0, n_max):
    Pn = [P0]  #Aqui vamos a almacenar los valores de Pn
    for n in range(n_max):
        Pn.append(a * Pn[-1] + b)
    return Pn

#Definimos los parametros
n_max = 50  #Definimos el número de iteraciones
P0 = 1  #Damos la condicion inicial

#Definimos varios valores de 'a' y 'b' para explorar diferentes comportamientos en la grafica
parametros = [(0.5, 0), (1.0, 0), (1.1, 0), (0.5, 0.5), (1.0, 0.5), (1.1, 0.5), (0.5, -0.5), (1.0, -0.5), (1.1, -0.5)]

#Damos las secuencias de Pn para cada conjunto de parámetros
plt.figure(figsize=(10, 8))
for a, b in parametros:
    Pn = sistema_dinamico(a, b, P0, n_max)
    plt.plot(Pn, label=f'a={a}, b={b}')

#Creamos la grafica de acuerdo a los parametros
plt.title('Comportamiento de Pn para diferentes valores de a y b')
plt.xlabel('n (iteraciones)')
plt.ylabel('Pn')
plt.legend()
plt.grid(True)
plt.show()

"""# EJERCICIO 2

**Estrategia de ahorro para comprar un Ipad**

Formula de crecimiento con interes compuesto: P_(n+1) = P_n (1+r) + ahorro_mensual

Donde:

*   𝑃_𝑛 es el capital acumulado en el mes n.
*   r es la tasa de interés mensual.
*   ahorro_mensual es la cantidad fija que se ahorra cada mes.

Supongamos que:

*  Costo del producto: 12,876 pesos
*  Intervalo de tiempo: 10 meses
*  Interés anual actual: 10.4%
*  Ahorros actuales: 500 pesos
*  Posible ahorro por mes: 250 pesos

"""

import numpy as np
import matplotlib.pyplot as plt

# Definimos el modelo de crecimiento de inversión con interés compuesto y ahorros mensuales
def crecimiento_ahorros(r, ahorro_mensual, P0, n_max):
    Pn = [P0]  # Capital inicial
    for n in range(n_max):
        Pn.append(Pn[-1] * (1 + r) + ahorro_mensual)
    return Pn

# Definimos los parametros
P0 = 500  # Ahorros iniciales
r = 0.104 / 12  # Interés mensual (10.4% anual)
ahorro_mensual = 250  # Ahorro mensual
n_max = 10  # Simulación para 10 meses
costo_producto = 12876  # Costo del iPad

# Generamos la secuencia de capitales acumulados
Pn_ahorros = crecimiento_ahorros(r, ahorro_mensual, P0, n_max)

# Verificamos si se alcanza el objetivo
monto_final = Pn_ahorros[-1]
if monto_final >= costo_producto:
    print(f"¡Lo lograste! En 10 meses ahorrarás {monto_final:.2f}, suficiente para comprar el iPad de {costo_producto}.")
else:
    print(f"No alcanzas el objetivo. En 10 meses ahorrarás {monto_final:.2f} , te faltan {costo_producto - monto_final:.2f} .")

# Graficamos el crecimiento de los ahorros
plt.figure(figsize=(8, 6))
plt.plot(Pn_ahorros, label=f'Ahorros acumulados: r={r:.4f}, Ahorro mensual={ahorro_mensual}')
plt.axhline(y=costo_producto, color='r', linestyle='--', label=f'Costo del producto: {costo_producto} ')
plt.title('Crecimiento de ahorros con interés compuesto')
plt.xlabel('Meses')
plt.ylabel('Ahorros acumulados')
plt.grid(True)
plt.legend()
plt.show()

"""Ahora, para poder cumplir con el plazo necesitariamos ahorrar 1,186 al mes."""

import numpy as np
import matplotlib.pyplot as plt

# Definimos el modelo de crecimiento de inversión con interés compuesto y ahorros mensuales
def crecimiento_ahorros(r, ahorro_mensual, P0, n_max):
    Pn = [P0]  # Capital inicial
    for n in range(n_max):
        Pn.append(Pn[-1] * (1 + r) + ahorro_mensual)
    return Pn

# Definimos los parámetros
P0 = 500  # Ahorros iniciales
r = 0.104 / 12  # Interés mensual (10.4% anual)
ahorro_mensual = 1186  # Ahorro mensual de 1,186 pesos
n_max = 10  # Simulación para 10 meses
costo_producto = 12876  # Costo del iPad

# Generamos la secuencia de capitales acumulados
Pn_ahorros = crecimiento_ahorros(r, ahorro_mensual, P0, n_max)

# Verificamos si se alcanza el objetivo
monto_final = Pn_ahorros[-1]
if monto_final >= costo_producto:
    print(f"¡Lo lograste! En 10 meses ahorrarás {monto_final:.2f}, suficiente para comprar el iPad de {costo_producto}.")
else:
    print(f"No alcanzas el objetivo. En 10 meses ahorrarás {monto_final:.2f}, te faltan {costo_producto - monto_final:.2f}.")

# Graficamos el crecimiento de los ahorros
plt.figure(figsize=(8, 6))
plt.plot(Pn_ahorros, label=f'Ahorros acumulados: r={r:.4f}, Ahorro mensual={ahorro_mensual}')
plt.axhline(y=costo_producto, color='r', linestyle='--', label=f'Costo del producto: {costo_producto}')
plt.title('Crecimiento de ahorros con interés compuesto')
plt.xlabel('Meses')
plt.ylabel('Ahorros acumulados')
plt.grid(True)
plt.legend()
plt.show()

"""Ahora, podemos ver distintos escenarios cambiando el ahorro inicial y el monto de ahorro al mes con el siguiente codigo."""

import numpy as np
import matplotlib.pyplot as plt

# Modelo de crecimiento de ahorros con interés compuesto y depósitos mensuales
def crecimiento_ahorros(interes_mensual, ahorro_mensual, capital_inicial, num_meses):
    capital = [capital_inicial]  # Capital inicial
    for mes in range(num_meses):
        capital.append(capital[-1] * (1 + interes_mensual) + ahorro_mensual)
    return capital

# Parámetros actualizados
capital_inicial = 500  # Ahorros iniciales
interes_mensual = 0.104 / 12  # Interés mensual (10.4% anual)
ahorro_mensual = 3500  # Ahorro mensual actualizado
num_meses = 24  # Simulación para 24 meses
costo_producto = 22999  # Costo del iPhone Plus

# Generamos la secuencia de capital acumulado
capital_ahorrado = crecimiento_ahorros(interes_mensual, ahorro_mensual, capital_inicial, num_meses)

# Verificamos si se alcanza el objetivo
monto_final = capital_ahorrado[-1]
if monto_final >= costo_producto:
    print(f"¡Lo lograste! En {num_meses} meses ahorrarás {monto_final:.2f}, suficiente para comprar el iPhone Plus de {costo_producto}.")
else:
    print(f"No alcanzas el objetivo. En {num_meses} meses ahorrarás {monto_final:.2f}, te faltan {costo_producto - monto_final:.2f}.")

# Graficamos el crecimiento de los ahorros
plt.figure(figsize=(8, 6))
plt.plot(capital_ahorrado, label=f'Ahorros acumulados: interés mensual={interes_mensual:.4f}, Ahorro mensual={ahorro_mensual}')
plt.axhline(y=costo_producto, color='r', linestyle='--', label=f'Costo del producto: {costo_producto}')
plt.title('Crecimiento de ahorros con interés compuesto')
plt.xlabel('Meses')
plt.ylabel('Ahorros acumulados')
plt.grid(True)
plt.legend()
plt.show()

# Link del producto
print(" https://www.apple.com/mx/shop/buy-iphone/iphone-16/pantalla-de-6.7-pulgadas-128gb-blanco")

# EJERCICIO 3
import numpy as np
import matplotlib.pyplot as plt

# Modelo de crecimiento de una inversión con interés y depósitos mensuales
def crecimiento_inversion(factor_crecimiento, deposito_mensual, capital_inicial, num_meses):
    capital = [capital_inicial]  # Capital inicial
    for mes in range(num_meses):
        capital.append(factor_crecimiento * capital[-1] + deposito_mensual)
    return capital

# Parámetros actualizados
capital_inicial_inversion = 22000  # Capital inicial actualizado
interes_anual = 0.05  # Tasa de interés anual
interes_mensual = interes_anual / 12  # Interés mensual
factor_crecimiento = 1 + interes_mensual  # Factor de crecimiento
deposito_mensual = 2760  # Depósito mensual actualizado
num_meses_inversion = 48  # Simulación para 48 meses

# Generamos la secuencia de capital acumulado
capital_inversion = crecimiento_inversion(factor_crecimiento, deposito_mensual, capital_inicial_inversion, num_meses_inversion)

# Graficamos el crecimiento de la inversión
plt.figure(figsize=(8, 6))
plt.plot(capital_inversion, label=f'Inversión: factor_crecimiento={factor_crecimiento:.4f}, depósito mensual={deposito_mensual}')
plt.title('Crecimiento de una inversión con interés y depósitos mensuales')
plt.xlabel('Meses')
plt.ylabel('Capital acumulado')
plt.grid(True)
plt.legend()
plt.show()


"""# Sitios utilizados



1.   https://www.cetesdirecto.com/calculadoras/ahorroRecurrente
2.   https://economipedia.com/definiciones/interes-compuesto.html
3.   https://www.elfinanciero.com.mx/mis-finanzas/2024/02/04/que-es-el-interes-compuesto-y-como-se-calcula/







"""