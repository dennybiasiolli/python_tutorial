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




print()
print('------------------ COSTRUZIONI DI LISTA ------------------')
# Le costruzioni di lista forniscono un modo conciso per creare liste senza ricorrere all'uso di map(), filter() e/o lambda.
# La definizione risultante è spesso più comprensibile di ciò che si ottiene con i costrutti accennati.
# Ogni costruzione di lista consiste di un'espressione a cui segue una clausola for, quindi zero o più clausole for o if.
# Il risultato sarà una lista creata valutando l'espressione nel contesto delle clausole for e if che la seguono.
# Se l'espressione valuta una tupla, questa dev'essere racchiusa tra parentesi.
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print("freshfruit: ", freshfruit)
print("res: ", [weapon.strip() for weapon in freshfruit])

vec = [2, 4, 6]
print("vec: ", vec)
print("res: ", [3*x for x in vec])
print("res: ", [3*x for x in vec if x > 3])
print("res: ", [3*x for x in vec if x < 2])
print("res: ", [[x,x**2] for x in vec])
print("res: ", [(x, x**2) for x in vec])

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print("vec1: ", vec1)
print("vec2: ", vec2)
print("res: ", [x*y for x in vec1 for y in vec2])
print("res: ", [x+y for x in vec1 for y in vec2])
print("res: ", [vec1[i]*vec2[i] for i in range(len(vec1))])
print("res: ", [str(round(355/113.0, i)) for i in range(1,6)])
del vec, vec1, vec2
