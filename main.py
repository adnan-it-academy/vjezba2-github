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
        return self.__stanje_na_racunu

    def get_dugovanja(self):
        """
        Vraća trenutna dugovanja korisnika.
        Implementirajte povrat vrijednosti privatnog atributa __dugovanja.
        """
        return self.__dugovanja

    def set_dugovanja(self, dug):
        """
        Postavlja novu vrijednost dugovanja.
        Implementirajte logiku za ažuriranje privatnog atributa __dugovanja.
        """
        self.__dugovanja = dug 

    # Metode za manipulaciju računom
    def uplata(self, iznos):
        """
        Uplaćuje određeni iznos na račun.
        Implementirajte provjeru da li je iznos veći od 0, a zatim dodajte iznos na __stanje_na_racunu.
        """
        if iznos > 0:
            self.__stanje_na_racunu += iznos

    def isplata(self, iznos):
        """
        Isplaćuje određeni iznos s računa.
        Implementirajte provjeru da li je iznos veći od 0 i da li ima dovoljno sredstava na računu.
        Ako su uvjeti ispunjeni, smanjite __stanje_na_racunu.
        """
        if iznos > 0 and iznos <= self.__stanje_na_racunu:
            self.__stanje_na_racunu -= iznos

    def provjeri_stanje(self):
        """
        Provjerava trenutno stanje na računu.
        Implementirajte ispis trenutnog stanja na računu u konzolu.
        """
        print(f"Trenutno stanje računa je {self.__stanje_na_racunu} KM")

    def dodaj_dugovanje(self, iznos):
        """
        Dodaje dugovanje korisniku.
        Implementirajte provjeru da li je iznos veći od 0, a zatim povećajte vrijednost __dugovanja.
        """
        if iznos > 0:
            self.__dugovanja += iznos

    def otplati_dugovanje(self, iznos):
        """
        Otplata dijela ili cjelokupnog dugovanja.
        Implementirajte provjeru da li je iznos validan (veći od 0 i manji ili jednak trenutnom dugu),
        a zatim umanjite __dugovanja.
        """
        if iznos > 0 and iznos <= self.__dugovanja:
            self.__dugovanja -= iznos

    # Metode za ažuriranje podataka korisnika
    def promijeni_broj_telefona(self, novi_broj):
        """
        Ažurira broj telefona korisnika.
        Implementirajte logiku za promjenu atributa broj_telefona.
        """
        self.broj_telefona = novi_broj

    def promijeni_email(self, novi_email):
        """
        Ažurira email adresu korisnika.
        Implementirajte logiku za promjenu atributa email.
        """
        self.email = novi_email

    # Metode za pregled informacija
    def prikazi_podatke(self):
        """
        Ispisuje osnovne informacije o korisniku.
        Implementirajte ispis svih atributa korisnika, uključujući privatne atribute.
        """
        print(f"Ime i prezime: {self.ime_prezime}\nGodište: {self.godiste}\nUlica: {self.ulica}\nBroj telefon: {self.broj_telefona}\nEmail: {self.email}\nStanje na racunu: {self.__stanje_na_racunu}\nDugovanje: {self.__dugovanja}")

    def je_li_duzan(self):
        """
        Provjerava da li korisnik ima dugovanja.
        Implementirajte povrat True ako su dugovanja veća od 0, inače False.
        """
        return True if self.__dugovanja > 0 else False


