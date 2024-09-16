def fibonacci(n):
    if n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Introduce el valor de n: ")) # secuencia de fibonacci hasta el numero n

fibonacci_sequence = [fibonacci(i) for i in range(n+1)]

print(f"La secuencia de Fibonacci hasta el término {n} es: {fibonacci_sequence}")
