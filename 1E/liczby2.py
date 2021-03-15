# Program drukuje dwucyfrowe liczby,
# przy czym liczby składające się
# z tych samych cyfr są pomijane,
# np. 11, 22, 33 itd.


for x in range(1, 10):
    for y in range(10):
        if x != y:
            print(f"xy = {x}{y}")
