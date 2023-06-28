

"""¿Un número es primo?"""
 
num = int(input("Escriba un numero y determinaré si es primo o no: "))
cont = 0
for i in range(num):
    if (num % (i+1)) == 0:
        cont += 1
if cont == 2 :
    print("Es un numero primo")
else:
    print("No es un numero primo")