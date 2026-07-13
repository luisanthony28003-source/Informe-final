# Problema 4.3
# Aproximar la derivada dV/dt en t = 30 s utilizando
# el método de diferencias finitas centradas

import numpy as np
import matplotlib.pyplot as plt

# Datos

t_anterior = 20.0      # Tiempo anterior (s)
t_central = 30.0       # Punto donde se desea calcular la derivada
t_posterior = 40.0     # Tiempo posterior (s)

V_anterior = 4.150     # Voltaje en 20 s
V_posterior = 4.710    # Voltaje en 40 s

# Tamaño del paso
h = 10.0

# Formula de diferencia centrada
dVdt_num = (V_posterior - V_anterior) / (2 * h)

# Para la derivada analitica

Vmax = 4.830
tau = 10.0

# Derivada exacta del modelo exponencial
dVdt_teo = (Vmax / tau) * np.exp(-t_central / tau)

# hallamos el error relativo

error = abs(dVdt_teo - dVdt_num) / dVdt_teo * 100

# resultados
print(" DERIVACIÓN NUMÉRICA")

print(f"Derivada numérica = {dVdt_num:.4f} V/s")
print(f"Derivada teórica  = {dVdt_teo:.4f} V/s")
print(f"Error relativo    = {error:.2f}%")

# Grafico
# Modelo exponencial de carga
t = np.linspace(0, 50, 400)
V = Vmax * (1 - np.exp(-t / tau))

# Pendiente numerica obtenida
V30 = Vmax * (1 - np.exp(-t_central / tau))

# Ecuacion de la recta tangente usando la derivada numérica
recta = V30 + dVdt_num * (t - t_central)

plt.figure(figsize=(8,5))

# Curva de carga del capacitor
plt.plot(
    t,
    V,
    linewidth=2,
    label="Curva de carga RC"
)

# Recta tangente aproximada
plt.plot(
    t,
    recta,
    '--',
    linewidth=2,
    label="Pendiente por diferencia centrada"
)

# Punto donde se calcula la derivada
plt.scatter(
    t_central,
    V30,
    s=80,
    zorder=5,
    label="t = 30 s"
)

# Nodos utilizados en la diferencia centrada
plt.scatter(
    [t_anterior, t_posterior],
    [V_anterior, V_posterior],
    s=70,
    zorder=5,
    label="Datos experimentales"
)

plt.title("Derivación Numérica por Diferencia Centrada")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje del capacitor (V)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
