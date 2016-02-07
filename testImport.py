import sys
import fattoriale, fibonacci, sommatoria

n = 10
if(len(sys.argv) > 1):
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Inserire un valore intero! Ora verrà impostato di default a", n, "\n")
else:
    print("Nessun parametro inserito, verrà impostato di default a", n, "\n")

print("Sommatoria da 1 a", n, " = ", sommatoria.get(n))
print("Fattoriale di", n, " = ", fattoriale.get(n))
print("Fibonacci per i primi", n, "numeri = ", fibonacci.fib(n))
