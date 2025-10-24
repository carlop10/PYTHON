import xml.etree.ElementTree as ET 
# Crear nodo raíz 
empresa = ET.Element("empresa") 
# Crear un empleado 
empleado = ET.SubElement(empresa, "empleado", id="1") 
ET.SubElement(empleado, "nombre").text = "Marta Díaz" 
ET.SubElement(empleado, "cargo").text = "Administradora" 
ET.SubElement(empleado, "salario").text = "4200" 
# Convertir a árbol y guardar 
arbol = ET.ElementTree(empresa) 
arbol.write("data/nuevo_empleado.xml", encoding="utf-8", xml_declaration=True) 
print("Archivo XML 'nuevo_empleado.xml' creado correctamente.")