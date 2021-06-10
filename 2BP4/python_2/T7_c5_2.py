def main():
    n = int(input("Podaj n: "))
    fib = 0
    if n<3 and n > 0:
        fib = 1
    else:
        p1 = p2 =1
        i = 3
        while i <= n:
            fib = p1 + p2
            p2 = p1
            p1 = fib
            i += 1
        
    print(f"F({n}) = {fib}")
    
    return 0

main()
