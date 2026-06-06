lista_productos = []
lista_precios = []

cantidad = int(input("¿Cuántos productos desea ingresar?: "))

for i in range(cantidad):
    producto = input(f"Ingrese el nombre del producto {i+1}: ")
    precio = float(input(f"Ingrese el precio de '{producto}': $"))

    lista_productos.append(producto)
    lista_precios.append(precio)
    
for i in range(len(lista_productos)):
    print(f" {lista_productos[i]:.<40} - ${lista_precios[i]}")

total = sum(lista_precios)
promedio = total / len(lista_precios)

print (f"El total es: ${total}")
print (f"El valor promedio por producto es: ${promedio}")
