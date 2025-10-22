from .hissi import Hissi

class Talo:
    def __init__(self,alinkerros, ylinkerros, hissien_lukumäärä):
        self.ylinkerros = ylinkerros
        self.alinkerros = alinkerros
        self.hissit = []
        self.hissien_lukumäärä = hissien_lukumäärä
        for i in range(hissien_lukumäärä):
            self.hissit.append(Hissi(self.alinkerros, self.ylinkerros))

    def aja_hissiä(self, hissinumero, kohdekerros):
        print(f"Ajat hissillä {hissinumero}")
        self.hissit[hissinumero - 1].siirry_kerrokseen(kohdekerros)



    def palohälytys(self):
        for i in range(self.hissien_lukumäärä):
            print(f"Hissi nunmero {i + 1}")
            self.hissit[i].siirry_kerrokseen(self.alinkerros)
