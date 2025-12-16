from ave import Ave
from mamifero import Mamifero

ave = Ave("Loro", 3, "Selva", "Herbívoro", "Pequeño", "Verde")
mamifero = Mamifero("Perro", 5, "Doméstico", "Omnívoro", "Mediano", "Café")

print(ave.moverse())
print(ave.comunicacion())

print(mamifero.moverse())
print(mamifero.alimentarse())
