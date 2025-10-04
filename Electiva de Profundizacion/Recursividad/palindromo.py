class fibo_recursividad:
    def __init__(self, palabra):
        self.palabra = palabra
        
    def es_palindromo(self, palabra):
        if len(palabra) <= 1:
            return True
        else:
            if palabra[0] == palabra[-1]:
                return self.es_palindromo(palabra[1:-1])
            else:
                return False
            
            
if __name__ == "__main__":
    palabra = "reconocer"
    pal = fibo_recursividad(palabra)
    res = pal.es_palindromo(palabra)
    print(f"La palabra: {palabra} es palindromo? = {res}")
