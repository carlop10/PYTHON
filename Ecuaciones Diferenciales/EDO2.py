import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# ======================
# Parámetros del sistema
# ======================
m, k, F0, omega = 1, 4, 2, 2  # masa, constante, fuerza, frecuencia
Y0 = [0, 0]  # y(0)=0, y'(0)=0

# Definición de la ecuación diferencial
def resorte(t, Y):
    y, yp = Y
    dydt = yp
    dypt = -(k/m)*y + (F0/m)*np.cos(omega*t)
    return [dydt, dypt]

# Resolver la ODE numéricamente
t_span = (0, 20)
t_eval = np.linspace(t_span[0], t_span[1], 2000)
sol = solve_ivp(resorte, t_span, Y0, t_eval=t_eval)

# ======================
# Configurar animación
# ======================
y_vals = sol.y[0]

fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 1)
ax.set_title("Animación: Masa-Resorte Forzado")
ax.set_xlabel("Posición")
ax.set_ylabel("Eje fijo")

# Dibujar línea del resorte + masa
spring_line, = ax.plot([], [], lw=2, color="blue")
mass = plt.Rectangle((0, -0.1), 0.2, 0.2, fc="red")
ax.add_patch(mass)

# Función para actualizar cada frame
def update(frame):
    x = y_vals[frame]  # desplazamiento de la masa
    # resorte desde pared en x=-2 hasta la masa
    spring_x = np.linspace(-2, x, 20)
    spring_y = 0.1 * np.sin(10 * np.linspace(0, 1, 20))
    spring_line.set_data(spring_x, spring_y)

    # actualizar masa
    mass.set_xy((x, -0.1))
    return spring_line, mass

ani = FuncAnimation(fig, update, frames=len(t_eval), interval=20, blit=True)

plt.show()
