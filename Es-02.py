#2) Trovo il fattoriale di un numero inserito in input
def fattoriale(n):
    if n==0 or n== 1:
        return 1
    else:
        return n * fattoriale(n-1)
number = int(input("Inserisci un numero: "))

print(fattoriale(number))
