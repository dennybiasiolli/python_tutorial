from functools import reduce

def add(x,y):
    return x+y

def get(n): return sommatoria(n)
def sommatoria(n):
    return reduce(add, range(1, n+1))
