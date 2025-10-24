# ejemplo_lectura_manual.py
archivo = open("data/ejemplo1.txt", "r", encoding="utf-8")  # Abrir archivo
contenido = archivo.read()  # Leer todo el contenido
print(contenido)
archivo.close()  # Cerrar el archivo (obligatorio sin 'with')
