import configparser 
 
config = configparser.ConfigParser() 
 
config["general"] = { 
    "app": "SistemaVentas", 
    "version": "1.0" 
} 
 
config["conexion"] = { 
    "host": "127.0.0.1", 
    "port": "3306", 
    "usuario": "admin", 
    "password": "secreto" 
} 
 
# Guardar en disco 
with open("data/config_creada.ini", "w") as archivo: 
    config.write(archivo) 
 
print("Archivo 'config_creada.ini' generado correctamente.")