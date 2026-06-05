lista_numeros = []
lista_evaluaciones = []

cantidad_numeros = int(input("¿Cuántos números va a ingresar en la lista?): "))

for i in range(cantidad_numeros):
    numero = float(input("Ingrese el número para ser evaluado posteriormente: "))
    lista_numeros.append(numero)

for numero in lista_numeros:
    if numero > 0:
        lista_evaluaciones.append("Es positivo")
    elif numero < 0:
        lista_evaluaciones.append("Es negativo")
    elif numero == 0:
        lista_evaluaciones.append("Es cero")

print (lista_evaluaciones)


                       