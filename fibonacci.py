# La serie di Fibonacci:
# la somma di due elementi definisce l'elemento successivo
import sys
l = 10
if(len(sys.argv) > 1):
    try:
        l = int(sys.argv[1])
    except ValueError:
        print("Inserire un valore intero!, Ora verrà impostato di default a 10")
print("Sequenza di Fibonacci per i primi " + str(l) + " numeri")
a, b, i = 0, 1, 0
while i < l:
    print(b)
    a, b, i = b, a+b, i+1