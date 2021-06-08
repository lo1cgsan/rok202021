def main():
    n = int(input("Podaj n: "))
    p1 = p2 = 1
    for i in range(3, n + 1):
        fib = p1 + p2
        p2 = p1
        p1 = fib

    print(f"F({n}) = {fib}")
    return 0

main()
