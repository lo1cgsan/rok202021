kody = ['.-', '-...', '-.-.', '-..', '.', '..-.']

def zakoduj(tekst):
    for l in tekst:
        if l == ' ':
            print('//', end='')
        else:
            print(kody[ord(l.lower()) - 97] + '/', end='')
    print()


def dekoduj(kod_morsea):
    for k in kod_morsea:
        print(chr(kody.index(k) + 97))
    print()


def main():
    tekst = input('Podaj tekst: ')
    zakoduj(tekst)
    kod_morsea = ['-..', '-...', '.']
    dekoduj(kod_morsea)
    return 0
    
main()
