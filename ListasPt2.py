#Listas parte 2

lista = [1,2,4,5,5,5,"Carolina"]

#Insertar elementos al último de la lista
lista.append(6)
#Insertar específicamente un lugar en la lista
lista.insert(2,3) #Primero se agrega la posición donde lo quieres agregar y luego el valor
#Insertar varios valores
lista.extend([6,7,8])

#Para saber si un valor está dentro de la lista
print(3 in lista)
#Para saber cuantas veces aparece el valor en la lista
print(lista.count(5))
#Para eliminar un valor en la lista escribiendo su indice
lista.pop(3)
#eliminar directamente un valor
lista.remove("Carolina")
#eliminar toda la lista
#lista.clear()
#Para que la lista quede volteada
lista.reverse()
#Para ordenar ascendentemente
lista.sort()


print(lista)
