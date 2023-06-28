def factorial(a):
    fac = 1
    for i in range(a):
        fac = fac * (i+1)
    return fac
num = int(input("Escriba el numero que quiere calcular: "))
print(f"El factorial de {num} es: {factorial(num)}")