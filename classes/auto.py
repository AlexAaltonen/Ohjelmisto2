class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0




    def kiihdytä(self, arvo):
        self.tämänhetkinen_nopeus += arvo
        if self.huippunopeus < self.tämänhetkinen_nopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0


        #tarkasta ettei nopeus ole yli huippunopeus
        #jos on, aseta nopeus = huippunopeus
        #tarkasta ettei nopeus ole alle 0
        #jos on, aseta nopeus = 0


    def kulje(self, aika):
        kuljettumatka = self.tämänhetkinen_nopeus * aika
        self.kuljettu_matka += kuljettumatka

        #laske kuinka paljon auto on kulkenut annetussa ajassa tietyllä nopeudella
        #lisää kuljettu matka kokonaismatkaan