from Aleix_B import book
from Aleix_B import user
from Aleix_B import university

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



