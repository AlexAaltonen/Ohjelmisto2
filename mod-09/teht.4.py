from classes.auto import Auto
import random
autot = []

for i in range(1, 11):
    # arvo huippunopeus 100 - 200
    huippunopeus =  random.randint(100, 200)
    autot.append(Auto("ABC-"+ str(i), huippunopeus))

kokonaismatka = 0

while kokonaismatka < 10000:
    for auto in autot:
        #arvo nopeuden muutos -10 - 15
        # kutsu kiihdytä
        auto.kulje(1)
        # hae matkan arvo, jos yli 10000, lopeta kisa asettamalla auton matka
        #kokonaismatkaksi


# googlaa joku taulukkokirjasto tulostamiseen

# ehkä metodi, joka palauttaa ominaisuudet dict / sanakirjana