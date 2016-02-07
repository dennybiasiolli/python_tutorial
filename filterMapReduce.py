print()
print('------------------ FILTER ------------------')
# "filter(funzione, sequenza)" restituisce una sequenza (dello stesso tipo, ove possibile) composta dagli elementi della sequenza originale per i quali è vera funzione(elemento). Per esempio, per calcolare alcuni numeri primi:
def f(x):
    return x % 2 != 0 and x % 3 != 0

a = range(2, 25)
print("Lista di numeri iniziale")
for i in a: print(i, "", end="")
print()

retVal = filter(f, a)
print("Lista di numeri dispari")
for i in retVal: print(i, "", end="")
print()




print()
print('------------------ MAP ------------------')
# "map(funzione, sequenza)" invoca funzione(elemento) per ciascuno degli elementi della sequenza e restituisce una lista dei valori ottenuti. Per esempio, per calcolare i cubi di alcuni numeri:
def cube(x):
    return x*x*x

a = range(1, 11)
print("Lista di numeri iniziale")
for i in a: print(i, "", end="")
print()
retVal = map(cube, a)
print("Lista del cubo dei numeri iniziali")
for i in retVal: print(i, "", end="")
print()




print()
print('------------------ REDUCE ------------------')
# "reduce(funzione, sequenza)" restituisce un singolo valore ottenuto invocando la funzione binaria (NdT: a due argomenti) funzione sui primi due elementi della sequenza, quindi sul risultato dell'operazione e sull'elemento successivo, e così via. Ad esempio, per calcolare la somma dei numeri da 1 a 10:
def add(x,y):
    return x+y

a = range(1, 11)
print("Lista di numeri iniziale")
for i in a: print(i, "", end="")
print()
from functools import reduce
retVal = reduce(add, a)
print("Somma dei numeri:", retVal)
