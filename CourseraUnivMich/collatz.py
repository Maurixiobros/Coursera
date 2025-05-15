# Hipótesis de Collatz

def collatz_sequence(n):
    """Genera la secuencia de Collatz para un número dado."""
    while n != 1:
        print(n, end=" -> ")
        if n % 2 == 0:  # Si es par
            n = n // 2
        else:  # Si es impar
            n = 3 * n + 1
    print(1)  # Imprimir el último número de la secuencia

# Solicitar un número entero positivo al usuario
try:
    num = int(input("Introduce un número entero positivo: "))
    if num > 0:
        print("Secuencia de Collatz:")
        collatz_sequence(num)
    else:
        print("Por favor, introduce un número mayor que 0.")
except ValueError:
    print("Entrada no válida. Por favor, introduce un número entero positivo.")