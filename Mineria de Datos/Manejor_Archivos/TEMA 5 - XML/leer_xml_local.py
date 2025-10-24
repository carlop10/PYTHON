import xml.etree.ElementTree as ET 
 
# Cargar el archivo XML 
arbol = ET.parse("data/empleados.xml") 
raiz = arbol.getroot() 
 
# Mostrar nombre del elemento raíz 
print("Elemento raíz:", raiz.tag) 
 
# Recorrer los elementos 
for emp in raiz.findall("empleado"): 
    id_emp = emp.get("id") 
    nombre = emp.find("nombre").text 
    cargo = emp.find("cargo").text 
    salario = float(emp.find("salario").text) 
    print(f"ID: {id_emp} | {nombre} - {cargo} - ${salario}") 