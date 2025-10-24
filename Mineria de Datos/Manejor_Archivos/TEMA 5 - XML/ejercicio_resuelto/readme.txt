5. Ejercicio resuelto (caso realista) 
Enunciado: 
 Tu empresa tiene un sistema que guarda los empleados en XML y necesita leer la 
configuración de conexión desde un .ini. 
 Debes cargar ambos, mostrar los datos y verificar si el puerto configurado es el correcto. 
Archivos: 
 config.ini 
[conexion] 
host = localhost 
port = 8080 
 
empleados.xml 
<empresa> 
    <empleado id="1"><nombre>Ana</nombre></empleado> 
<empleado id="2"><nombre>Luis</nombre></empleado> 
</empresa> 