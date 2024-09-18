#3) Dizionario: {"a": 1, "b": 2, "c": 3}, scambio la posizione tra chiave e valore
dictionary = {"a": 1, "b": 2, "c": 3}

for key, value in enumerate(dictionary):
    t = key
    key = value
    value = t

print(dictionary)