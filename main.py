class KorisnickiNalog:
    """
    Klasa koja predstavlja korisnički nalog sa osnovnim podacima i funkcionalnostima.
    """

    def __init__(self, ime_prezime, godiste, ulica, broj_telefona, email, stanje_na_racunu):
        """
        Konstruktor klase. Inicijalizuje osnovne atribute korisnika.
        """
        self.ime_prezime = ime_prezime
        self.godiste = godiste
        self.ulica = ulica
        self.broj_telefona = broj_telefona
        self.email = email
        self.__stanje_na_racunu = stanje_na_racunu  # Privatni atribut
        self.__dugovanja = 0  # Privatni atribut (početna vrijednost)

    # GET i SET metode za privatne atribute
    def get_stanje_na_racunu(self):
        """
        Vraća trenutno stanje na računu.
        Implementirajte povrat vrijednosti privatnog atributa __stanje_na_racunu.
        """
        pass

    def get_dugovanja(self):
        """
        Vraća trenutna dugovanja korisnika.
        Implementirajte povrat vrijednosti privatnog atributa __dugovanja.
        """
        pass

    def set_dugovanja(self, dug):
        """
        Postavlja novu vrijednost dugovanja.
        Implementirajte logiku za ažuriranje privatnog atributa __dugovanja.
        """
        pass

    # Metode za manipulaciju računom
    def uplata(self, iznos):
        """
        Uplaćuje određeni iznos na račun.
        Implementirajte provjeru da li je iznos veći od 0, a zatim dodajte iznos na __stanje_na_racunu.
        """
        pass

    def isplata(self, iznos):
        """
        Isplaćuje određeni iznos s računa.
        Implementirajte provjeru da li je iznos veći od 0 i da li ima dovoljno sredstava na računu.
        Ako su uvjeti ispunjeni, smanjite __stanje_na_racunu.
        """
        pass

    def provjeri_stanje(self):
        """
        Provjerava trenutno stanje na računu.
        Implementirajte ispis trenutnog stanja na računu u konzolu.
        """
        pass

    def dodaj_dugovanje(self, iznos):
        """
        Dodaje dugovanje korisniku.
        Implementirajte provjeru da li je iznos veći od 0, a zatim povećajte vrijednost __dugovanja.
        """
        pass

    def otplati_dugovanje(self, iznos):
        """
        Otplata dijela ili cjelokupnog dugovanja.
        Implementirajte provjeru da li je iznos validan (veći od 0 i manji ili jednak trenutnom dugu),
        a zatim umanjite __dugovanja.
        """
        pass

    # Metode za ažuriranje podataka korisnika
    def promijeni_broj_telefona(self, novi_broj):
        """
        Ažurira broj telefona korisnika.
        Implementirajte logiku za promjenu atributa broj_telefona.
        """
        pass

    def promijeni_email(self, novi_email):
        """
        Ažurira email adresu korisnika.
        Implementirajte logiku za promjenu atributa email.
        """
        pass

    # Metode za pregled informacija
    def prikazi_podatke(self):
        """
        Ispisuje osnovne informacije o korisniku.
        Implementirajte ispis svih atributa korisnika, uključujući privatne atribute.
        """
        pass

    def je_li_duzan(self):
        """
        Provjerava da li korisnik ima dugovanja.
        Implementirajte povrat True ako su dugovanja veća od 0, inače False.
        """
        pass
