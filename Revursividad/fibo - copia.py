class fibo_recursividad:
    def __init__(self, n):
        self.n = n
        self.contador = 0  # contador de llamadas
    
    def fibo(self, n, prefijo="", es_ultimo=True):
        self.contador += 1
        rama = "└─" if es_ultimo else "├─"
        print(f"{prefijo}{rama} Llamada {self.contador}: fibo({n})")
        
        if n <= 1:
            print(f"{prefijo}   => Retorna 0")
            return 0
        elif n == 2:
            print(f"{prefijo}   => Retorna 1")
            return 1
        else:
            # Para los hijos ajustamos prefijos
            nuevo_prefijo = prefijo + ("   " if es_ultimo else "│  ")
            valor1 = self.fibo(n - 1, nuevo_prefijo, False)
            valor2 = self.fibo(n - 2, nuevo_prefijo, True)
            valor = valor1 + valor2
            print(f"{prefijo}   => Retorna {valor} (fibo({n}))")
            return valor

if __name__ == "__main__":
    n = 8
    fib = fibo_recursividad(n)
    resultado = fib.fibo(n)
    print(f"\n-- El Fibonacci de {n} es: {resultado}")
    print(f"-- Total de llamados recursivos: {fib.contador}")
