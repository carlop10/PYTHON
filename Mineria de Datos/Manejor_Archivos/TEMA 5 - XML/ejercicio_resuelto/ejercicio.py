import configparser 
import xml.etree.ElementTree as ET 
# Leer configuración 
config = configparser.ConfigParser() 
config.read("data/config.ini") 
puerto = config["conexion"].getint("port") 
# Leer XML 
arbol = ET.parse("data/empleados.xml") 
raiz = arbol.getroot() 
print("Puerto configurado:", puerto) 
print("Empleados registrados:") 
for emp in raiz.findall("empleado"): 
    print("-", emp.find("nombre").text) 
# Validación 
if puerto == 8080: 
    print(" ✅ El puerto es correcto (8080).") 
else: 
    print(" ⚠ Puerto incorrecto.") 