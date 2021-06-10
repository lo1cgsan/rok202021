def main():
    n = int(input("Podaj n: "))
    p1 = p2 = fib = 1
    for i in range(3, n + 1):
        fib = p1 + p2
        p2 = p1
        p1 = fib

    print(f"F({n}) = {fib}")
    return 0

main()

"""
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
"""
