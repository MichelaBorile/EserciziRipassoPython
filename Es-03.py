#3) Dizionario: {"a": 1, "b": 2, "c": 3}, scambio la posizione tra chiave e valore
dictionary = {"a": 1, "b": 2, "c": 3}
dictionary_reverse ={}
for i in dictionary:
    dictionary_reverse.setdefault(dictionary[i], i)

print(dictionary_reverse)