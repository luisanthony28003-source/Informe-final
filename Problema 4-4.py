# Problema 4.4 
# Calcular el área bajo la curva del voltaje del capacitor
# desde t = 0 s hasta t = 60 s.

import numpy as np
import matplotlib.pyplot as plt

# Datos

t = np.array([0, 2, 5, 10, 20, 30, 60], dtype=float)

V = np.array([
    0.000,
    0.390,
    1.630,
    2.970,
    4.150,
    4.550,
    4.830
], dtype=float)

# Regla del trapecio compuesta
# Variable donde se acumulará el area total
area_total = 0

print(" REGLA DEL TRAPECIO COMPUESTA")

# Se calcula el area de cada trapecio
for i in range(1, len(t)):

    # Base del trapecio
    h = t[i] - t[i-1]

    #   Area del trapecio
    area = (V[i-1] + V[i]) * h / 2

    # Se acumula el area total
    area_total += area

    print(f"Intervalo {i}:")
    print(f"Tiempo = {t[i-1]:.0f} s a {t[i]:.0f} s")
    print(f"Área = {area:.3f} V·s")
    print("-----------------------------")

# El voltaje promedio

tiempo_total = t[-1] - t[0]

V_promedio = area_total / tiempo_total

# Valor teorico

Vmax = 4.830
tau = 10

# Integral exacta del modelo exponencial
integral_teorica = Vmax * (
    tiempo_total
    + tau * np.exp(-tiempo_total/tau)
    - tau
)

V_prom_teorico = integral_teorica / tiempo_total

# Error relativo

error = abs(V_prom_teorico - V_promedio) / V_prom_teorico * 100

print("\n RESULTADOS ")

print(f"Área total = {area_total:.3f} V·s")
print(f"Voltaje promedio = {V_promedio:.4f} V")
print(f"Voltaje promedio teórico = {V_prom_teorico:.4f} V")
print(f"Error relativo = {error:.2f}%")

# garfico
# Curva experimental
plt.figure(figsize=(9,5))

plt.plot(
    t,
    V,
    marker='o',
    linewidth=2,
    label="Datos experimentales"
)

# Area bajo la curva
plt.fill_between(
    t,
    V,
    alpha=0.3,
    label="Área integrada"
)

plt.title("Integración Numérica mediante la Regla del Trapecio")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje del capacitor (V)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
