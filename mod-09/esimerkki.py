class Koira:

    def __init__(self, nimi, syntymävuosi):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi

koira1 = Koira("Rekku", 2022)
koira2 = Koira("Seppo", 2002)

print (f"{koira1.nimi:s} on syntynyt vuonna {koira1.syntymävuosi:d}." )
print (f"{koira2.nimi:s} on syntynyt vuonna {koira2.syntymävuosi:d}." )

class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.haukahdus)
        return


koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")

koira1.hauku(2)
koira2.hauku(5)
