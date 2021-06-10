import math

def f_liniowa(x):
    return x + 1
    
def f_wykladnicza(x, k):
    return x**k

def f_silnia(x):
    return math.factorial(x)
    
lx = range(10)
ly1 = []
ly2 = []
ly3 = []
for x in lx:
    ly1.append(f_liniowa(x))
    ly2.append(f_wykladnicza(x, 2))
    ly3.append(f_silnia(x))


print(ly1)
print(ly2)
print(ly3)
