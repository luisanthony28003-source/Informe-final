# Metodo de Runge-Kutta de Cuarto Orden (RK4)
# Problema 4.5 - Descarga 
# Simular la descarga del capacitor resolviendo la
# ecuación diferencial dV/dt = -V/(RC) mediante el método RK4.

import numpy as np
import matplotlib.pyplot as plt

# Parsmetros 

R = 10000          # Resistencia (ohms)
C = 0.001          # Capacitancia (F)

tau = R * C        # Constante de tiempo RC

# Condición inicial
V0 = 4.830         # Voltaje inicial (V)

# Tiempo inicial y final
t0 = 0
tf = 60

# Paso de integración
h = 2.0

# La ecuacion diferernciañ

def f(t, V):
    """
    Ecuación diferencial de descarga del capacitor.

    dV/dt = -V/(RC)
    """
    return -V / tau

# Metodo RK4
# Vector de tiempos
t = np.arange(t0, tf + h, h)

# Vector de los voltajes
V = np.zeros(len(t))

# Condicion inicial
V[0] = V0

print(" MÉTODO RUNGE-KUTTA DE CUARTO ORDEN")

# Bucle principal de integracion
for i in range(len(t)-1):

    # Primera pendiente
    k1 = f(t[i], V[i])

    # Segunda pendiente
    k2 = f(
        t[i] + h/2,
        V[i] + (h/2)*k1
    )

    # Tercera pendiente
    k3 = f(
        t[i] + h/2,
        V[i] + (h/2)*k2
    )

    # Cuarta pendiente
    k4 = f(
        t[i] + h,
        V[i] + h*k3
    )

    # Formula de Runge-Kutta
    V[i+1] = V[i] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

    # Mostrar cada iteracion
    print(f"Paso {i+1}")
    print(f"Tiempo = {t[i+1]:.0f} s")
    print(f"Voltaje = {V[i+1]:.4f} V")
    print("--------------------------")

# Comparacion de valores
# Valor experimental a los 2 segundos
V_real = 4.150

# Valor calculado por RK4
V_calc = V[1]

# Error relativo
error = abs(V_real - V_calc)/V_real * 100

print("\n========== RESULTADOS ==========")

print(f"Voltaje RK4 en t=2 s = {V_calc:.4f} V")
print(f"Voltaje experimental = {V_real:.4f} V")
print(f"Error relativo = {error:.2f}%")

# Solucion exacta de la EDO
V_teorica = V0 * np.exp(-t/tau)

# Graficamos

plt.figure(figsize=(9,5))

# Solucion RK4
plt.plot(
    t,
    V,
    'o-',
    linewidth=2,
    label="Solución RK4"
)

# Solucion analitica
plt.plot(
    t,
    V_teorica,
    '--',
    linewidth=2,
    label="Solución analítica"
)

# Punto experimental
plt.scatter(
    2,
    V_real,
    s=90,
    zorder=5,
    label="Dato experimental"
)

plt.title("Descarga del capacitor mediante Runge-Kutta de 4.º Orden")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
