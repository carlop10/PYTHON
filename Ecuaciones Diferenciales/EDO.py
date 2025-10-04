import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from sympy import Function, dsolve, Eq, Derivative, symbols, cos

# ======================
# Parte 1: Sympy (resolver la EDO analíticamente)
# ======================
t = symbols('t')
y = Function('y')

# EDO: y'' + 4y = 2cos(2t)
edo = Eq(Derivative(y(t), t, 2) + 4*y(t), 2*cos(2*t))
sol_general = dsolve(edo)
print("Solución general analítica:")
print(sol_general)

# ======================
# Parte 2: Simulación numérica
# ======================
m, k, F0, omega = 1, 4, 2, 2

def resorte(t, Y):
    y, yp = Y
    dydt = yp
    dypt = -(k/m)*y + (F0/m)*np.cos(omega*t)
    return [dydt, dypt]

# Condiciones iniciales
Y0 = [0, 0]  # y(0)=0, y'(0)=0

# Intervalo de simulación
t_span = (0, 20)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Resolver numéricamente
sol = solve_ivp(resorte, t_span, Y0, t_eval=t_eval)

# ======================
# Parte 3: Graficar
# ======================
plt.figure(figsize=(9,4))
plt.plot(sol.t, sol.y[0], label="Posición de la masa")
plt.xlabel("Tiempo (s)")
plt.ylabel("Desplazamiento")
plt.title("Movimiento de un resorte forzado (y'' + 4y = 2cos(2t))")
plt.grid(True)
plt.legend()
plt.show()

