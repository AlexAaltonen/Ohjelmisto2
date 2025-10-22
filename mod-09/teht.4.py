from classes.auto import Auto
import random
from tabulate import tabulate

autot = []
for i in range(1, 11):
    # arvo huippunopeus 100 - 200
    huippunopeus =  random.randint(100, 200)
    autot.append(Auto("ABC-"+ str(i), huippunopeus))

kokonaismatka = 0

while kokonaismatka < 10000:
    for auto in autot:
        #arvo nopeuden muutos -10 - 15
        auton_nopeus = random.randint(-10, 15)
        # kutsu kiihdytä
        auto.kiihdytä(auton_nopeus)
        auto.kulje(1)
        if auto.kuljettu_matka > kokonaismatka:
            kokonaismatka = auto.kuljettu_matka

        # hae matkan arvo, jos yli 10000, lopeta kisa asettamalla auton matka
        #kokonaismatkaksi

tilanne_taulukko = []
for auto in autot:
    tilanne_taulukko.append([auto.rekisteritunnus,
                            f"{auto.tämänhetkinen_nopeus} km/h",
                            f"{auto.kuljettu_matka} km"])
print(tabulate(tilanne_taulukko, headers = ["Nimi","Nopeus","Matka"], tablefmt="grid"))


# googlaa joku taulukkokirjasto tulostamiseen
# https://www.datacamp.com/tutorial/python-tabulate

# ehkä metodi, joka palauttaa ominaisuudet dict / sanakirjana