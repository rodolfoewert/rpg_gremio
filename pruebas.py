from personajes import Personaje, Guerrero
from objetos import Objeto

g = Guerrero("Roland", 30, 8)
g.recibir_daño(50)
print(g.get_vida())      # debe dar 0, no -20

#Personaje("x", 10)       # debe dar TypeError (bórrala después de probarla)
#Objeto("x").describir()  # debe dar NotImplementedError