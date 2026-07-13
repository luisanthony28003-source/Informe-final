# INTERPOLACION DE NEWTON DE SEGUNDO ORDEN
# Problema 4.1 
# Objetivo: Estimar el voltaje del capacitor en t = 25 s

import numpy as np
import matplotlib.pyplot as plt

# Datos 
# Tres nodos cercanos al punto que se desea interpolar tiempo y voltaje

t = np.array([15.0, 20.0, 30.0])      
V = np.array([3.760, 4.150, 4.550])   

# Valor donde se desea estimar el voltaje
t_obj = 25.0

# Valor real medido
V_real = 4.430

# Primer coeficiente
b0 = V[0]

# Primera diferencia dividida entre los dos primeros puntos
b1 = (V[1] - V[0]) / (t[1] - t[0])

# Primera diferencia dividida entre el segundo y tercer punto
f12 = (V[2] - V[1]) / (t[2] - t[1])

# Segunda diferencia dividida (representa la curvatura del polinomio)
b2 = (f12 - b1) / (t[2] - t[0])

# Polinomio de Newton

def newton_p2(x):
    """
    Evalúa el polinomio de Newton de segundo orden
    para cualquier valor de tiempo x.
    """
    return (
        b0
        + b1 * (x - t[0])
        + b2 * (x - t[0]) * (x - t[1])
    )

# la evaluacion en el punto

V_calc = newton_p2(t_obj)

# Error relativo

error = abs(V_real - V_calc) / V_real * 100

# resultados obtenidos

print(" RESULTADOS ")
print(f"b0 = {b0:.4f}")
print(f"b1 = {b1:.6f} V/s")
print(f"b2 = {b2:.6f} V/s²")
print()
print(f"Voltaje interpolado en t = {t_obj:.1f} s")
print(f"V({t_obj:.1f}) = {V_calc:.4f} V")
print()
print(f"Voltaje experimental = {V_real:.4f} V")
print(f"Error relativo = {error:.3f}%")

# Hacemos un grafico para comparar las soluciones
# Se generan muchos puntos para dibujar una curva suave.
t_graf = np.linspace(15, 30, 300)
V_graf = newton_p2(t_graf)

plt.figure(figsize=(8,5))

# Curva del polinomio interpolador
plt.plot(
    t_graf,
    V_graf,
    label="Polinomio de Newton",
    linewidth=2
)

# Nodos experimentales utilizados
plt.scatter(
    t,
    V,
    color="red",
    s=70,
    label="Datos experimentales",
    zorder=5
)

# Punto interpolado
plt.scatter(
    t_obj,
    V_calc,
    color="green",
    s=90,
    label="Voltaje interpolado",
    zorder=6
)

# Valor experimental real
plt.scatter(
    t_obj,
    V_real,
    color="black",
    marker="x",
    s=100,
    label="Valor real",
    zorder=6
)

# Linea vertical para identificar el instante buscado
plt.axvline(
    x=t_obj,
    linestyle="--",
    linewidth=1
)

plt.title("Interpolación de Newton de Segundo Orden")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje del capacitor (V)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
