from Aleix_B import book
from Aleix_B import user
from Aleix_B import university
from ExerciciA import animal
from ExerciciA import vehicle
from ExerciciA import school

l1 = book(" Harry Potter", " Pablo Rosado", " Norma Editorial", " 345", " Dura", " Català \n")
l1.informacio()
l1.setAutor(" Carlos Sanchez") #Modifica les dades d'un objecte
l1.informacio()

l2 = book(" Ets galàctica, Carlota", " Edgar Romero", " Catalonia Editorial", " 268", " Tova", " Català \n")
l2.informacio()
l2.setPagines(" 459")
l2.informacio()

u1 = user(" Aleix", " Alvarez", " 20", " 21778592F", " aalvarez22@jaumebalmes.net", " Gigabyte \n")
u1.info()
u1.setNom(" Marc")
u1.info()

u2 = user(" Joan", " Gago", " 19", " 23423442W", " jgago22@jaumebalmes.net", " Gigabyte \n")
u2.info()
u2.setEdat(" 45")
u2.info()

uni1 = university(" Oxford", " Anglaterra", " 534", " 100", " 15", " 3000€ \n")
uni1.informa()
uni1.setLloc(" Espanya")
uni1.informa()

uni2 = university(" Harvard", " Estats Units", " 683", " 150", " 20", " 5000€ \n")
uni2.informa()
uni2.setPreu(" 3500€")
uni2.informa()

a1 = animal("Puma", "Carn", "4 anys", "Gris", "Mamifer", "Mascle \n")
a2 = animal("Lleó", "Carn", "7 anys", "Daurada", "Mamifer", "Femella \n")
a1.text()
a2.text()
a1.setEdat("3 anys")
a2.setSexe("Mascle")
a1.text()
a2.text()

v1 = vehicle("Ford Falcon", "Gasolina", "100.000", "Blau", "Deportiu", "112 \n")
v2 = vehicle("Honda Civic", "Diesel", "50.000", "Negre", "4x4", "190 \n")
v1.text2()
v2.text2()
v1.setColor("Vermell")
v2.setKilometres("0")
v1.text2()
v2.text2()

s1 = school("Escuela Secundaria Sor Maria Josefa Rossello", "Irurtia 8258", "Escola Secundaria Obligatoria", "3", "540", "50 \n")
s2 = school("Institut Viladomat", "C. del Consell de Cent, 148", "Escola Secundaria Obligatoria", "4", "620", "55  \n")
s1.text3()
s2.text3()
s1.setAlumnes("700")
s2.setLinies("3")
s1.text3()
s2.text3()

