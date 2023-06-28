import random
"""
a = "amigo"

for i in a:
    print(f"Dame una '{i}'")
print(a)
"""
""" -----------For con rango------------- """
"""
fois = int(input("¿Cuantas veces quiere que le salude?"))
for i in range(fois):
    print(f"{i} ", end="")
print()
print("adios") 
"""
"""-------------For con Random-------------"""
"""



print("Comienzo")
sacaste_cinco = False
for i in range(3):
    dado = random.randrange(1, 7)
    print(f"Tirada {i + 1}: {dado}")
    if dado == 5:
        sacaste_cinco = True
if sacaste_cinco:
    print("Ha salido al menos un 5.")
else:
    print("No ha salido ningún 5.")
print("Final")
"""
"""-------------Contador----------------"""

"""
print("Comienzo")
cuenta_cincos = 0
for i in range(3):
    dado = random.randrange(1, 7)
    print(f"Tirada {i + 1}: {dado}")
    if dado == 5:
        cuenta_cincos += 1
if cuenta_cincos == 0:
        print("No salió ningún cinco")
else:    
        print(f"En total, ha(n) salido {cuenta_cincos} cinco(s).")
print("Final")
"""
"""------------While---------------"""

i = 1
while i <= 50:
    print(i)
    i = 2 * i + 1
print("Programa terminado")