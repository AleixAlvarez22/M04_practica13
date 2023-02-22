class university:
    def __init__(self, nom, lloc, alumnes, profesors, aules, preu): #Crea un constructor
        self.nom = nom
        self.lloc = lloc
        self.alumnes = alumnes
        self.professors = profesors
        self.aules = aules
        self.preu = preu

    def getNom(self):
        return self.nom #Crea un getter

    def setNom(self, nom):  #Crea un setter
        self.nom = nom

    def getLloc(self):
        return self.lloc

    def setLloc(self, lloc):
        self.lloc = lloc

    def getAlumnes(self):
        return self.alumnes

    def setAlumnes(self, alumnes):
        self.alumnes = alumnes

    def getProfessors(self):
        return self.professors

    def setProfessors(self, profesors):
        self.professors = profesors

    def getAules(self):
        return self.aules

    def setAules(self, aules):
        self.aules = aules

    def getPreu(self):
        return self.preu

    def setPreu(self, preu):
        self.preu = preu

    def informa(self):
        print("Universitat:" + self.nom)
        print("Lloc:" + self.lloc)
        print("Te:" + self.alumnes + " alumnes")
        print("Te:" + self.professors + " professors")
        print("Te:" + self.aules + " aules")
        print("Te un preu de:" + self.preu)


