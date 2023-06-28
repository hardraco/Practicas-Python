"""--------------Funcion con parametros definidos----------"""
"""
def escribe_media(x, y):
    media = (x + y) / 2
    print(f"La media de {x} y {y} es: {media}")
    return

a = 3
b = 5
escribe_media(a, b)
print("Programa terminado")
"""
"""---------Funcion con parametros no definidos------------"""

def promedio(x,y,z):
    prome = (x+y+z) / 3
    print(f"El promedio de las notas es: {prome}")
    return

nota1 = int(input("1ra Nota: "))
nota2 = int(input("2da Nota: "))
nota3 = int(input("3ra Nota: "))

promedio(nota1,nota2,nota3)
print("Fin del programa")