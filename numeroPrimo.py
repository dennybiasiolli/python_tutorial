import sys

# controlla se n è un numero primo
def isPrimo(n):
    for x in range(2, n):
        if n % x == 0:
            # print(n, 'non è un numero primo, è uguale a', x, '*', int(n/x))
            return False
            break
    else:
        # Il ciclo scorre la sequenza senza trovare il fattore
        # print(n, 'è un numero primo')
        return True

n = 191
if(len(sys.argv) > 1):
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Inserire un valore intero! Ora verrà impostato di default a 10\n")
else:
    print("Nessun parametro inserito, verrà impostato di default a", n, "\n")

if(isPrimo(n)):
    print(n, 'è un numero primo')
else:
    print(n, 'non è un numero primo')