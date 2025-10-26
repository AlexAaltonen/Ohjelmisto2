from classes.auto import Auto, Sahkoauto, Polttomoottioriauto

sahkoauto =Sahkoauto("ABC-123", 200, 52.5)
polttomoottoriauto = Polttomoottioriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdytä(190)
polttomoottoriauto.kiihdytä(90)

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauton mittarilukema: {sahkoauto.kuljettu_matka}")
print(f"Polttomoottoriauton mittarilukema: {polttomoottoriauto.kuljettu_matka}")

