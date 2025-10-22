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
        auton_nopeus = random.randint(-10, 15)
        # kutsu kiihdytä
        auto.kiihdytä(auton_nopeus)
        auto.kulje(1)
        if auto.kuljettu_matka > kokonaismatka:
            kokonaismatka = auto.kuljettu_matka

        # hae matkan arvo, jos yli 10000, lopeta kisa asettamalla auton matka
        #kokonaismatkaksi


for auto in autot:
    print(f'''Auton rekisteritunnus: {auto.rekisteritunnus}
    Auton huippunopeus: {auto.huippunopeus} km/h
    Auton tämänhetkinen nopeus: {auto.tämänhetkinen_nopeus} km/h
    Auton kuljettu matka: {auto.kuljettu_matka} km''')
    print()


# googlaa joku taulukkokirjasto tulostamiseen

# ehkä metodi, joka palauttaa ominaisuudet dict / sanakirjana