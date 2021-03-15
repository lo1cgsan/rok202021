
def liczby2():
    for i in range(1, 10):
        for j in range(0, 10):
            if i != j:
                print(f"{i}{j}")

# i > j or i < j
# i != j
def main():
    liczby2()
    return 0


main()
