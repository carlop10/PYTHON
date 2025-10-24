import os

print("Usuario:", os.getlogin())  # nombre del usuario actual
print("CWD:", os.getcwd())  # directorio de trabajo actual
os.chdir("../data")  # cambiar al directorio 'data'
print("Nuevo CWD:", os.getcwd())  # nuevo directorio de trabajo
