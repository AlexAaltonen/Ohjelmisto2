from classes.auto import Auto

auto1 = Auto("ABC-123", 142)

auto1.kiihdytä(70)
auto1.kulje(2)





print(f'''Auton rekisteritunnus: {auto1.rekisteritunnus}
Auton huippunopeus: {auto1.huippunopeus} km/h
Auton tämänhetkinen nopeus: {auto1.tämänhetkinen_nopeus} km/h
Auton kuljettu matka: {auto1.kuljettu_matka} km''')

auto1.kiihdytä(-200)

print(f'''Auton rekisteritunnus: {auto1.rekisteritunnus}
Auton huippunopeus: {auto1.huippunopeus} km/h
Auton tämänhetkinen nopeus: {auto1.tämänhetkinen_nopeus} km/h
Auton kuljettu matka: {auto1.kuljettu_matka} km''')