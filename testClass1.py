class MiaClasse:
    """Una semplice classe d'esempio"""
    i = 12345
    __priv1 = 'settordici' 
    def f(self):
        return 'ciao mondo' + ' --> ' + self.__priv1
    def __init__(self, i):
        self.i = i
        self.data = []

class MiaClasse2(MiaClasse):
    """Estensione della classe 1"""
    def test(self):
        return 'funziona alla perfezione!'
    # def test2(self):
    #     return self.__priv1 # genera eccezione perché è una variabile privata della classe base

x = MiaClasse(12)
print(x.__doc__)
print(x.i)
# print(x.__priv1) # genera eccezione perché è una variabile privata della classe
print(x.f())

x.counter = 1
print(x.counter)
del x.counter

y = MiaClasse2(334)
print(y.__doc__)
print(y.i)
print(y.f())
print(y.test())