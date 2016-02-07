import sys

# La serie di Fibonacci:
# la somma di due elementi definisce l'elemento successivo
def fib(n):
    """Restituisce la serie di Fibonacci fino a n"""
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(b)    # vedi sotto
        a, b = b, a+b
    return result


l = 10
if(len(sys.argv) > 1):
    try:
        l = int(sys.argv[1])
    except ValueError:
        print("Inserire un valore intero! Ora verrà impostato di default a 10\n")
else:
    print("Nessun parametro inserito, verrà impostato di default a 10\n")
print(fib.__doc__)
print("Sequenza di Fibonacci per i primi " + str(l) + " numeri")
print(fib(l))