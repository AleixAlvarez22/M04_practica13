
class vehicle:  # Declarm la classe
    def __init__(self, marca, combustible, kilometres, color, tipus, cavalls):  # Creem el constructor i els atributs
        self.marca = marca
        self.combustible = combustible
        self.kilometres = kilometres
        self.color = color
        self.tipus = tipus
        self.cavalls = cavalls

    def getMarca(self):  # Creem getter
        return self.marca

    def setMarca(self, marca):  # Creem setter
        self.marca = marca

    def getCombustible(self):
        return self.combustible

    def setCombustible(self, combustible):
        self.combustible = combustible

    def getKilometres(self):
        return self.kilometres

    def setKilometres(self, kilometres):
        self.kilometres = kilometres

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getTipus(self):
        return self.tipus

    def setTipus(self, tipus):
        self.tipus = tipus

    def getCavalls(self):
        return self.cavalls

    def setCavalls(self, cavalls):
        self.cavalls = cavalls

    def text2(self):
        print("Marca: " + self.marca)
        print("Combustible: " + self.combustible)
        print("Kilometres: " + self.kilometres)
        print("Color: " + self.color)
        print("Tipus: " + self.tipus)
        print("Cavalls: " + self.cavalls)


