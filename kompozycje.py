class Dysk:
    def __init__(self, pojemnosc, typdysku, maxodczytu, maxzapisu) -> None:
        self.typdysku = typdysku
        self.pojemnosc = pojemnosc
        self.maxodczytu = maxodczytu
        self.maxzapisu = maxzapisu

    def infdysk(self):
       return f"typ dysku: {self.typdysku}, pojemnosc: {self.pojemnosc}, maksymalna predkosc odczytu: {self.maxodczytu}, maksymalna predkosc zapisu: {self.maxzapisu}"



class Zasilacz:
    def __init__(self, moc) -> None:
        self.moc = moc

    def infzasilacz(self):
        return f"moc zasilacza: {self.moc}"
          


class Chlodzenie:
    def __init__(self, rodzaj) -> None:
        self.rodzaj = rodzaj

    def infchlodzenie(self):
        return f"rodzaj chlodzenia procesora: {self.rodzaj}"
        


class PlytaGlowna:
    def __init__(self, format, maxpamiec, rodzajpamieci) -> None:
        self.format = format
        self.maxpamiec = maxpamiec
        self.rodzajpamieci = rodzajpamieci

    def infplytaglowna(self):
        return f"format: {self.format}, maksymalna wielkosc pamieci: {self.maxpamiec}, rodzaj pamieci: {self.rodzajpamieci}"
  


class Komputer:
    def __init__(self, dysk: Dysk, zasilacz: Zasilacz, chlodzenie: Chlodzenie, plytaglowna: PlytaGlowna) -> None:
        self.dysk = dysk
        self.zasilacz = zasilacz
        self.chlodzenie = chlodzenie
        self.plytaglowna = plytaglowna

    def infdyskprint(self):
        return self.dysk.infdysk
    
    def infzasilaczprint(self):
        return self.zasilacz.infzasilacz
    
    def infchlodzenieprint(self):
        return self.chlodzenie.infchlodzenie
    
    def infplytaglownaprint(self):
        return self.plytaglowna.infplytaglowna




dysk = Dysk("SSD", "wewnetrzny", "520 MB/s", "450 MB/s")
zasilacz = Zasilacz(850)
chlodzenie = Chlodzenie("powietrzne")
plytaglowna = PlytaGlowna("ATX", "128 GB", "DDR 5")
komputer = Komputer(dysk, zasilacz, chlodzenie, plytaglowna)
print(komputer.infdyskprint())
print(komputer.infzasilaczprint())
print(komputer.infchlodzenieprint())
print(komputer.infplytaglownaprint())