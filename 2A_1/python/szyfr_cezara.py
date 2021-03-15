
def szyfruj(tekst, k):
    k = k % 26
    k = 3
    szyfrogram = ''
    for znak in tekst:
        (a)97-(z)122
        
        ord(z) + k > 122
            ord(z) + k - 26
        szyfrogram += chr(ord(a) + k)
    

def main():
    tekst = input("Podaj tekst: ")
    klucz = int(input("Podaj klucz: "))
    szyfruj(tekst, klucz)
    return 0
