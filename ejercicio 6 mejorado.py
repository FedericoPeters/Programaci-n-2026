import random

lista_numeros = []

for i in range(3):
    var_aleatoria = random.randint(1, 99)
    lista_numeros.append(var_aleatoria)



maximo = 0
for cada_numero in lista_numeros:
    if cada_numero > maximo:
        maximo = cada_numero

print("Los números generados son:", lista_numeros)
print("El número mayor es:", maximo)    