#1) Da lista1 = [1, 2, 3, 4, 5], creo lista2 che ha tutti i valori raddoppiati
lista1 =[1, 2, 3, 4, 5]

for i in lista1:
    lista2 =[number *2 for number in lista1]

print(lista2)