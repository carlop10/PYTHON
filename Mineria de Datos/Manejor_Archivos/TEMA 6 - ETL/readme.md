 Objetivo general 
Comprender y aplicar el proceso ETL (Extract, Transform, Load) utilizando los módulos 
estándar de Python para procesar datos en múltiples formatos de archivo, tanto locales 
como remotos. 
�
�
 1. Teoría: ¿Qué es un proceso ETL? 
ETL significa: 
Fase 
E – Extracción 
T – 
Transformación 
L – Carga 
Descripción 
Obtención de datos desde 
diversas fuentes. 
Limpieza, validación, y 
transformación de datos. 
Almacenamiento de los datos 
transformados. 
Ejemplo 
Leer archivos TXT, CSV, JSON, 
XML o APIs. 
Eliminar duplicados, convertir 
tipos, agregar cálculos. 
Guardar como nuevo archivo 
CSV o JSON. 
�
�
 2. Herramientas estándar que usaremos 
Tipo de 
archivo 
TXT 
CSV 
JSON 
XML 
INI 
Módulo de Python 
open() 
csv 
json 
xml.etree.Element
 Tree 
configparser 
Propósito 
Lectura y escritura básica 
Tablas estructuradas 
Datos estructurados 
jerárquicos 
Datos con etiquetas 
jerárquicas 
Configuración y parámetros 
⚙
 3. Caso práctico ETL (ejemplo realista) 
�
�
 Escenario: 
Una pequeña empresa quiere consolidar la información de ventas de sus sucursales. 
● Cada sucursal guarda sus datos en diferentes formatos: 
○ Sucursal 1: archivo ventas_1.csv 
○ Sucursal 2: archivo ventas_2.json 
○ Sucursal 3: archivo ventas_3.txt 
● Un archivo de configuración (config.ini) define: 
 
○ El impuesto IVA (%) 
 
○ La moneda 
 
● El objetivo es unificar todas las ventas, calcular el total con IVA, y guardar el 
resultado en un archivo XML final (ventas_finales.xml). 
 
 
�
�
 Archivos de ejemplo 
�
�
 Archivo 1: ventas_1.csv 
id,producto,cantidad,precio 
1,Teclado,3,25000 
2,Mouse,5,12000 
3,Pantalla,2,150000 
 
�
�
 Archivo 2: ventas_2.json 
[ 
    {"id": 4, "producto": "USB", "cantidad": 10, "precio": 8000}, 
    {"id": 5, "producto": "Cámara", "cantidad": 1, "precio": 220000} 
] 
 
�
�
 Archivo 3: ventas_3.txt 
id,producto,cantidad,precio 
6,Auriculares,2,45000 
7,Microfono,1,60000 
 
⚙
 Archivo de configuración: config.ini 
[general] 
iva = 0.19 
moneda = COP