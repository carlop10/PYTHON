import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.integrate import solve_ivp
import tkinter as tk
from tkinter import messagebox
import sys
import tkinter.font as font

class ResorteApp:
    def __init__(self, root):
        self.root = root
        root.title("Simulador Masa-Resorte Forzado, By: Carlos Lopez - Ecuaciones Diferenciales")
        root.resizable(True, True)
        root.grid_rowconfigure(7, weight=1) # Permitir que la fila 7 (gráfico) se expanda
        root.grid_columnconfigure(1, weight=1) # Permitir que la columna 1 (gráfico) se expanda
        root.configure(bg="lightyellow", padx=10, pady=10, bd=5, relief="ridge")


        # Definir una fuente común
        self.fuente_general = font.Font(family="Times New Roman", size=11)
        self.fuente_boton = font.Font(family="Times New Roman", size=10, weight="bold")

        # Entradas
        tk.Label(root, text="Masa (m)", bg ="lightyellow", font=self.fuente_general).grid(row=0, column=0, sticky="w")
        tk.Label(root, text="Constante (k)", bg ="lightyellow", font=self.fuente_general).grid(row=1, column=0, sticky="w")
        tk.Label(root, text="Fuerza (F0)", bg ="lightyellow", font=self.fuente_general).grid(row=2, column=0, sticky="w")
        tk.Label(root, text="Frecuencia (ω)", bg ="lightyellow", font=self.fuente_general).grid(row=3, column=0, sticky="w")

        self.entry_m = tk.Entry(root, font=self.fuente_general); self.entry_m.grid(row=0, column=1, sticky="w", padx=5, pady=1)
        self.entry_k = tk.Entry(root, font=self.fuente_general); self.entry_k.grid(row=1, column=1, sticky="w", padx=5, pady=1)
        self.entry_F0 = tk.Entry(root, font=self.fuente_general); self.entry_F0.grid(row=2, column=1, sticky="w", padx=5, pady=1)
        self.entry_omega = tk.Entry(root, font=self.fuente_general); self.entry_omega.grid(row=3, column=1, sticky="w", padx=5, pady=1)

        # Valores por defecto
        self.entry_m.insert(0, "1")
        self.entry_k.insert(0, "4")
        self.entry_F0.insert(0, "2")
        self.entry_omega.insert(0, "2")

        frame_buttons = tk.Frame(root, bg="lightyellow")
        frame_buttons.grid(row=0, column=2, rowspan=4 , sticky="nsew")

        # Botones a la derecha de los inputs
        tk.Button(frame_buttons, text="Ejecutar", font=self.fuente_boton, command=self.run_simulation).grid(row=0, column=0, sticky="ew", pady=(0,5), ipadx=10)
        tk.Button(frame_buttons, text="Detener", font=self.fuente_boton, command=self.stop_animation).grid(row=1, column=0, sticky="ew", pady=(0,5), ipadx=10)
        tk.Button(frame_buttons, text="Reanudar", font=self.fuente_boton, command=self.start_animation).grid(row=2, column=0, sticky="ew", pady=(0,5), ipadx=10)
        tk.Button(frame_buttons, text="Salir", font=self.fuente_boton, command=self.exit_app).grid(row=3, column=0, sticky="ew", pady=(0,5), ipadx=10)

        # Marco donde se insertará la figura
        self.plot_frame = tk.Frame(root)
        self.plot_frame.grid(row=7, column=0, columnspan=3, sticky="nsew")  # ahora ocupa 3 columnas
        root.grid_rowconfigure(7, weight=1)
        root.grid_columnconfigure(1, weight=1)


        self.canvas = None
        self.fig = None
        self.ani = None

    def run_simulation(self):
        try:
            m = float(self.entry_m.get())
            k = float(self.entry_k.get())
            F0 = float(self.entry_F0.get())
            omega = float(self.entry_omega.get())
            if m == 0:
                raise ValueError("m no puede ser 0")
        except ValueError as e:
            messagebox.showerror("Error", f"Valores inválidos: {e}")
            return

        def resorte(t, Y):
            y, yp = Y
            return [yp, -(k/m)*y + (F0/m)*np.cos(omega*t)]

        t_span = (0, 20)
        t_eval = np.linspace(t_span[0], t_span[1], 1000)
        sol = solve_ivp(resorte, t_span, [0, 0], t_eval=t_eval, rtol=1e-6)
        y_vals = sol.y[0]

        if self.ani is not None:
            try:
                self.ani.event_source.stop()
            except Exception:
                pass
            self.ani = None
        if self.canvas is not None:
            self.canvas.get_tk_widget().destroy()
            plt.close(self.fig)
            self.canvas = None
            self.fig = None

        # Línea vertical negra en la posición 0
        
        self.fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        max_disp = max(1.0, np.max(np.abs(y_vals)))
        x_limit = max(2.0, max_disp * 1.5)
        ax1.set_xlim(-x_limit, x_limit)
        ax1.set_ylim(-max(0.5, max_disp * 0.5), max(0.5, max_disp * 0.5))
        ax1.set_title("Masa-Resorte Forzado")
        ax1.set_xlabel("Posición")
        ax1.set_ylabel("Eje fijo")
        wall_x = -x_limit
        ax1.axvline(wall_x, color="black", lw=2)
        ax1.axvline(0, color="black", lw=1, ls="--")

        spring_line, = ax1.plot([], [], lw=2)
        mass_w, mass_h = 0.25, 0.15
        mass = plt.Rectangle((0 - mass_w/2, -mass_h/2), mass_w, mass_h, fc="red")
        ax1.add_patch(mass)

        ax2.set_xlim(t_span)
        y_margin = 0.5
        ax2.set_ylim(np.min(y_vals) - y_margin, np.max(y_vals) + y_margin)
        ax2.set_title("Desplazamiento en el tiempo")
        ax2.set_xlabel("Tiempo")
        ax2.set_ylabel("y(t)")
        line_disp, = ax2.plot([], [], lw=1.5)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=1)

        def update(frame):
            x = y_vals[frame]
            spring_x = np.linspace(wall_x + mass_w/2, x - mass_w/2, 20)
            spring_y = 0.08 * np.sin(10 * np.linspace(0, 1, spring_x.size))
            spring_line.set_data(spring_x, spring_y)
            mass.set_xy((x - mass_w/2, -mass_h/2))
            line_disp.set_data(t_eval[:frame], y_vals[:frame])
            self.canvas.draw_idle()
            return spring_line, mass, line_disp

        self.ani = FuncAnimation(self.fig, update, frames=len(t_eval), interval=20, blit=False)

    def stop_animation(self):
        if self.ani is not None:
            self.ani.event_source.stop()

    def start_animation(self):
        if self.ani is not None:
            self.ani.event_source.start()

    def exit_app(self):
        if self.ani is not None:
            try:
                self.ani.event_source.stop()
            except Exception:
                pass
        self.root.destroy()
        plt.close("all")
        sys.exit(0)

def main():
    root = tk.Tk()
    app = ResorteApp(root)
    root.geometry("800x600")
    root.mainloop()

if __name__ == "__main__":
    main()
