import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# ======================
# Parámetros del sistema
# ======================
m, k, F0, omega = 1, 4, 2, 2  # masa, constante, fuerza, frecuencia
Y0 = [0, 0]  # y(0)=0, y'(0)=0

# Ecuación diferencial: y'' + (k/m)y = (F0/m)cos(omega t)
def resorte(t, Y):
    y, yp = Y
    dydt = yp
    dypt = -(k/m)*y + (F0/m)*np.cos(omega*t)
    return [dydt, dypt]

# Resolver la ODE
t_span = (0, 20)
t_eval = np.linspace(t_span[0], t_span[1], 1000)
sol = solve_ivp(resorte, t_span, Y0, t_eval=t_eval)
y_vals = sol.y[0]

# ======================
# Configurar la figura
# ======================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# --- Gráfico animación resorte ---
ax1.set_xlim(-2, 2)
ax1.set_ylim(-1, 1)
ax1.set_title("Masa-Resorte Forzado")
ax1.set_xlabel("Posición")
ax1.set_ylabel("Eje fijo")

spring_line, = ax1.plot([], [], lw=2, color="blue")
mass = plt.Rectangle((0, -0.1), 0.2, 0.2, fc="red")
ax1.add_patch(mass)

# --- Gráfico desplazamiento ---
ax2.set_xlim(t_span)
ax2.set_ylim(min(y_vals)-0.5, max(y_vals)+0.5)
ax2.set_title("Desplazamiento en el tiempo")
ax2.set_xlabel("Tiempo")
ax2.set_ylabel("y(t)")
line_disp, = ax2.plot([], [], color="green")

# ======================
# Función de actualización
# ======================
def update(frame):
    x = y_vals[frame]

    # Actualizar resorte
    spring_x = np.linspace(-2, x, 20)
    spring_y = 0.1 * np.sin(10 * np.linspace(0, 1, 20))
    spring_line.set_data(spring_x, spring_y)
    mass.set_xy((x, -0.1))

    # Actualizar desplazamiento
    line_disp.set_data(t_eval[:frame], y_vals[:frame])

    return spring_line, mass, line_disp

ani = FuncAnimation(fig, update, frames=len(t_eval), interval=20, blit=True)

plt.tight_layout()
plt.show()
