from functools import reduce

def mult(x,y):
    return x*y

def get(n): return fattoriale(n)
def fattoriale(n):
    return reduce(mult, range(1, n+1))


# n = 10
# if(len(sys.argv) > 1):
#     try:
#         n = int(sys.argv[1])
#     except ValueError:
#         print("Inserire un valore intero! Ora verrà impostato di default a", n, "\n")
# else:
#     print("Nessun parametro inserito, verrà impostato di default a", n, "\n")
# 
# print(fattoriale(n))
