# Problema 4.2 
# Determinar el instante en que el capacitor alcanza
# un voltaje de 4.000 V durante la carga

import numpy as np
import matplotlib.pyplot as plt

# Parametros experimentales

Vmax = 4.830      # Voltaje final de régimen permanente
tau = 10.0        # Constante de tiempo RC (s)
V_obj = 4.000     # Voltaje objetivo

# Definición de la función f(t)
# La raíz ocurre cuando f(t)=0

def f(t):
    """
    Función cuyo cero representa el instante
    en que el capacitor alcanza 4.000 V.
    """
    return Vmax * (1 - np.exp(-t/tau)) - V_obj

# Derivada de la función para el Newton Raphson

def df(t):
    """
    Derivada de f(t)
    """
    return (Vmax/tau) * np.exp(-t/tau)

# Aproximación inicial
t0 = 15.0

# Tolerancia de convergencia
tol = 1e-4

# Numero máximo de iteraciones
max_iter = 20

print(" MÉTODO DE NEWTON-RAPHSON")

for i in range(max_iter):

    # Formula iterativa
    t1 = t0 - f(t0)/df(t0)

    # Error absoluto entre iteraciones
    error = abs(t1 - t0)

    print(f"Iteración {i+1}")
    print(f"t = {t1:.6f} s")
    print(f"Error = {error:.6f}")
    print("------------------------")

    # Verificar convergencia
    if error < tol:
        break

    # Actualizar valor para la siguiente iteración
    t0 = t1

# Resultado final
t_calc = t1

print("\nRESULTADO FINAL")
print(f"Tiempo calculado = {t_calc:.4f} s")

# Comparación con el valor experimental

t_real = 18.0

error_rel = abs(t_real - t_calc)/t_real * 100

print(f"Tiempo experimental = {t_real:.2f} s")
print(f"Error relativo = {error_rel:.2f}%")

# graficamos
# Curva de carga exponencial
t = np.linspace(0, 50, 500)

V = Vmax * (1 - np.exp(-t/tau))

plt.figure(figsize=(8,5))

# Curva de carga del capacitor
plt.plot(
    t,
    V,
    linewidth=2,
    label="Modelo de carga RC"
)

# Linea horizontal del voltaje objetivo
plt.axhline(
    y=V_obj,
    linestyle="--",
    linewidth=1.5,
    label="Voltaje objetivo = 4.000 V"
)

# Linea vertical en el tiempo calculado
plt.axvline(
    x=t_calc,
    linestyle="--",
    linewidth=1.5,
    label=f"t calculado = {t_calc:.2f} s"
)

# Punto de interseccion
plt.scatter(
    t_calc,
    V_obj,
    s=80,
    zorder=5,
    label="Raíz encontrada"
)

plt.title("Método de Newton-Raphson para hallar el tiempo de cruce")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje del capacitor (V)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
