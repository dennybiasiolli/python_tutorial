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
