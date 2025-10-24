import configparser 
config = configparser.ConfigParser() 
config.read("data/config.ini") 
print("Aplicación:", config["general"]["app"]) 
print("Versión:", config["general"]["version"]) 
print("Usuario BD:", config["base_datos"]["user"]) 