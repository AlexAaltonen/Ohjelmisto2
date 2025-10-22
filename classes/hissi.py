class Hissi:

    def __init__(self, alinkerros, ylinkerros):
        self.ylinkerros = ylinkerros
        self.alinkerros = alinkerros
        self.kerros = alinkerros

    def siirry_kerrokseen(self, kerros):
        if self.kerros > self.ylinkerros:
            print("kerros ei ole sallittujen rajojen sisällä.")
        elif self.kerros < self.alinkerros:
            print("kerros ei ole sallittujen rajojen sisällä.")

        while self.kerros < kerros:
            self.kerros_ylös()
        while self.kerros > kerros:
            self.kerros_alas()
        print(f"hissi on kerroskessa {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1

    def kerros_ylös(self):
        self.kerros += 1