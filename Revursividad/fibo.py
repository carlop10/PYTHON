class fibo_recursividad:
    def __init__(self, n):
        self.n = n
        self.contador = 0
        
    def fibo(self, n):
        self.contador += 1
        print(f"Llamado #{self.contador}: F({n})") 
        if n <= 1:
            return 0
        else:
            if n == 2:
                return 1
            else:
                return self.fibo(n - 1) + self.fibo(n - 2)

if __name__ == "__main__":
    n = 8
    fib = fibo_recursividad(n)
    resultado = fib.fibo(n)
    print(f"\nEl Fibonacci de {n} es: {resultado}")
    print(f"Total de llamados recursivos: {fib.contador}")
