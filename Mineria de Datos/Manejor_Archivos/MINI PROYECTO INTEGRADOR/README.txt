Título: Sistema de Gestión de Empleados — Consolidación de Datos desde Múltiples 
Formatos 


Objetivo general 
Aplicar los conocimientos adquiridos sobre lectura, escritura y conversión de archivos TXT, 
CSV y JSON utilizando únicamente las bibliotecas estándar de Python (csv, json, os, 
urllib). 

Contexto del problema (caso realista) 
Una empresa pequeña lleva la información de sus empleados en distintos formatos: 
● Una lista inicial en TXT con nombres y correos. 
● Un archivo CSV con información adicional (edad, cargo, salario). 
● Una fuente JSON en la nube con datos sobre el estado de los empleados (activos o 
inactivos). 
Tu tarea es unificar toda la información en un solo archivo maestro JSON, realizando 
validaciones y cálculos básicos. 


 Archivos del proyecto 
1⃣ empleados.txt 
Ana Gómez,ana.gomez@empresa.com 
Luis Pérez,luis.perez@empresa.com 
Marta Díaz,marta.diaz@empresa.com 
2⃣ info_empleados.csv 
nombre,edad,cargo,salario 
Ana Gómez,30,Ingeniera de Software,4500 
Luis Pérez,25,Analista de Datos,3800 
Marta Díaz,27,Administradora,4200 
3⃣ Fuente JSON en la nube (disponible públicamente) 

 https://jsonplaceholder.typicode.com/users 
Solo utilizaremos los nombres que coincidan para obtener el campo address.city (la 
ciudad). 

 Objetivos específicos 
1. Leer y procesar información desde archivos TXT, CSV y JSON (remoto). 
2. Combinar los datos en una sola estructura unificada (lista de diccionarios). 
3. Validar la existencia de campos y completar los faltantes con valores 
predeterminados. 
4. Guardar el resultado consolidado en un archivo empleados_completo.json. 
5. Mostrar un resumen con estadísticas básicas (promedio de salario, número de 
empleados activos, etc.). 