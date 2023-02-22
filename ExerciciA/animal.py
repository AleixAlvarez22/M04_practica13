
class animal:  # Declarm la classe
    def __init__(self, nom, alimentacio, edat, pelatge, tipus, sexe):  # Creem el constructor i els atributs
        self.nom = nom
        self.alimentacio = alimentacio
        self.edat = edat
        self.pelatge = pelatge
        self.tipus = tipus
        self.sexe = sexe

    def getNom(self): # Creem getter
        return self.nom

    def setNom(self, nom):  # Creem setter
        self.nom = nom

    def getAlimentacio(self):
        return self.alimentacio

    def setAlimentacio(self, alimentacio):
        self.alimentacio = alimentacio

    def getEdat(self):
        return self.edat

    def setEdat(self, edat):
        self.edat = edat

    def getPelatge(self):
        return self.pelatge

    def setPelatge(self, pelatge):
        self.pelatge = pelatge

    def getTipus(self):
        return self.tipus

    def setTipus(self, tipus):
        self.tipus = tipus

    def getSexe(self):
        return self.sexe

    def setSexe(self, sexe):
        self.sexe = sexe

    def text(self):
        print("Nom: " + self.nom)
        print("Alimentació: " + self.alimentacio)
        print("Edat: " + self.edat)
        print("Pelatge: " + self.pelatge)
        print("Tipus: " + self.tipus)
        print("Sexe: " + self.sexe)
