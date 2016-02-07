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




