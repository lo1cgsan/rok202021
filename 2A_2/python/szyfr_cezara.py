

def szyfruj(tekst, klucz):
    klucz %= 26
    for znak in tekst:
        # ASCII: a(97)..z(122)
        ord(znak) + klucz > 122
        spacja
        print(chr(ord(znak) + klucz))


def main():
    tekst = input("Podaj tekst: ")
    klucz = int(input("Podaj klucz: "))
    szyfruj(tekst)
    
    return 0
    
    
main()
