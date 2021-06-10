import math

def liniowa(*x):
    return x
    
def wykladnicza(*x, k=2):
    return x**k

def silnia(*x):
    return math.factorial(x)

liczby = range(10)

print(list(liczby))
print(liniowa(liczby))
print(wykladnicza(liczby))
print(silnia(liczby))
exit
for l in liczby:
    print(liniowa(l),'', end='')

print()
for l in liczby:
    print(wykladnicza(l, 2),'', end='')

print()
for l in liczby:
    print(silnia(l),'', end='')
