class user:
    def __init__(self, nom, cognom, edat, dni, mail, treball): #Crea un constructor
        self.nom = nom
        self.cognom = cognom
        self.edat = edat
        self.dni = dni
        self.mail = mail
        self.treball = treball

    def getNom(self):  #Crea un getter
        return self.nom

    def setNom(self, nom):  #Crea un setter
        self.nom = nom

    def getCognom(self):
        return self.cognom

    def setCognom(self, cognom):
        self.cognom = cognom

    def getEdat(self):
        return self.edat

    def setEdat(self, edat):
        self.edat = edat

    def getDni(self):
        return self.dni

    def setDni(self, dni):
        self.dni = dni

    def getMail(self):
        return self.mail

    def setMail(self, mail):
        self.mail = mail

    def getTreball(self):
        return self.treball

    def setTreball(self, treball):
        self.treball = treball

    def info(self):
        print("El meu nom és:" + self.nom)
        print("El meu cognom és:" + self.cognom)
        print("Tinc:" + self.edat + " anys")
        print("El meu DNI és:" + self.dni)
        print("El meu correu és:" + self.mail)
        print("Treballo de:" + self.treball)

