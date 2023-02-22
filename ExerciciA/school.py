
class school:  # Declarm la classe
    def __init__(self, nom, direccio, estudis, linies, alumnes, profesorat):  # Creem el constructor i els atributs
        self.nom = nom
        self.direccio = direccio
        self.estudis = estudis
        self.linies = linies
        self.alumnes = alumnes
        self.profesorat = profesorat

    def getNom(self):  # Creem getter
        return self.nom

    def setNom(self, nom):  # Creem setter
        self.nom = nom

    def getDireccio(self):
        return self.direccio

    def setDireccio(self, direccio):
        self.direccio = direccio

    def setEstudis(self):
        return self.estudis

    def setEstudis(self, estudis):
        self.estudis = estudis

    def setLinies(self):
        return self.linies

    def setLinies(self, linies):
        self.linies = linies

    def getAlumnes(self):
        return self.alumnes

    def setAlumnes(self, alumnes):
        self.alumnes = alumnes

    def getProfesorat(self):
        return self.cavalls

    def setProfesorat(self, profesorat):
        self.profesorat = profesorat

    def text3(self):
        print("Nom: " + self.nom)
        print("Direcció: " + self.direccio)
        print("Estudis: " + self.estudis)
        print("Linies: " + self.linies)
        print("Alumnes: " + self.alumnes)
        print("Profesorat: " + self.profesorat)



