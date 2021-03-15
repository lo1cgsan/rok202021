class Osoba:

    def __init__(self, imie = '', nazwisko = ''):
        self.imie = imie
        self.nazwisko = nazwisko
        self.__ustawPlec()
        self.min_length = 2


    def __ustawPlec(self):
        try:
            if self.imie[-1] == 'a':
                self.plec = 'k'
            else:
                self.plec = 'm'
        except:
            self.plec = ''
    
    def set_Imie(self, imie):
        if len(imie.strip()) > self.min_length:
            self.imie = imie.strip()
        else:
            print("Błędne dane!")
    
    
    def get_Imie(self):
        return self.imie
            
