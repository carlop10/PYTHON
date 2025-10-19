import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# Parámetros fijos del ejemplo
m, k, F0, omega = 1, 4, 2, 2

# Ecuación diferencial del sistema
def resorte(t, Y):
    y, yp = Y
    return [yp, -(k/m)*y + (F0/m)*np.cos(omega*t)]

# Resolver numéricamente
t_span = (0, 20)
t_eval = np.linspace(*t_span, 1000)
sol = solve_ivp(resorte, t_span, [0, 0], t_eval=t_eval)
y_vals = sol.y[0]

# Crear figura con dos subgráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
fig.canvas.manager.set_window_title("Ejemplo: Sistema Masa–Resorte Forzado | EDO Grupo 3")

# ----- Configuración del gráfico de movimiento -----
max_disp = np.max(np.abs(y_vals))
x_limit = max(2.0, max_disp * 1.8)
ax1.set_xlim(-x_limit, x_limit)
ax1.set_ylim(-0.5, 0.5)
ax1.set_title("Movimiento masa–resorte forzado", fontsize=10)
ax1.set_xlabel("Posición")
ax1.set_ylabel("Eje fijo")

# Pared y eje de referencia
wall_x = -x_limit
ax1.axvline(wall_x, color="black", lw=2)
ax1.axvline(0, color="black", lw=1, ls="--")

# Elementos gráficos: resorte y masa
spring_line, = ax1.plot([], [], lw=2)
mass_w = 0.15 * x_limit
mass_h = 0.15
mass = plt.Rectangle((0 - mass_w/2, -mass_h/2), mass_w, mass_h, fc="red", ec="black")
ax1.add_patch(mass)

# ----- Configuración del gráfico de desplazamiento -----
ax2.set_xlim(t_span)
ax2.set_ylim(np.min(y_vals) - 0.5, np.max(y_vals) + 0.5)
ax2.set_title("Desplazamiento en el tiempo", fontsize=10)
ax2.set_xlabel("Tiempo")
ax2.set_ylabel("y(t)")
line_disp, = ax2.plot([], [], lw=1.5, color="blue")

# Mostrar fórmula y parámetros dentro de la figura
fig.text(0.5, 0.95, r"$m\,y'' + k\,y = F_0 \cos(\omega t)$", 
         ha="center", va="top", fontsize=12, style='italic')

fig.text(0.5, 0.01, 
         f"Parámetros:  m = {m},  k = {k},  F₀ = {F0},  ω = {omega}", 
         ha="center", fontsize=10, color="gray")

# ----- Función de actualización de la animación -----
def update(frame):
    x = y_vals[frame]
    spring_x = np.linspace(wall_x + mass_w/2, x - mass_w/2, 20)
    spring_y = 0.08 * np.sin(10 * np.linspace(0, 1, spring_x.size))
    spring_line.set_data(spring_x, spring_y)
    mass.set_xy((x - mass_w/2, -mass_h/2))
    line_disp.set_data(t_eval[:frame], y_vals[:frame])
    return spring_line, mass, line_disp

# Animar
ani = FuncAnimation(fig, update, frames=len(t_eval), interval=20, blit=False)
plt.tight_layout(rect=[0, 0.03, 1, 0.9])  # deja espacio arriba para la fórmula
plt.show()
