# Programa que calcula la nota media de tres asignaturas

nota1 = float(input("Introduce la primera nota: "))
nota2 = float(input("Introduce la segunda nota: "))
nota3 = float(input("Introduce la tercera nota: "))

media = (nota1 + nota2 + nota3) / 3
media = round(media, 2)

# Si la media termina en .0 o .00, muestra solo un decimal.
if media.is_integer():
    print(f"La nota media es: {int(media)}")
else:
    # Si tiene hasta 2 decimales, elimina ceros innecesarios
    print(f"La nota media es: {media:.2f}".rstrip('0'))

if media >= 5:
    print("Has aprobado")
else:
    print("Has suspendido")