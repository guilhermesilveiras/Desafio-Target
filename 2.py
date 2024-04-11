
def verifica_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return 'O número informado pertence à sequência de Fibonacci!'
        a, b = b, a+b
    return 'O número informado não pertence à sequência de Fibonacci!'

numero = int(input())
print(verifica_fibonacci(numero))