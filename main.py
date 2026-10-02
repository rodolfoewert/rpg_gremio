from personajes import Guerrero, Mago
from objetos import Arma, Usable, Gema

# --- Crear el personaje ---
print("=== Creación de personaje ===")
nombre = input("Nombre del personaje: ")
tipo = input("¿Guerrero (1) o Mago (2)? ")
vida = int(input("Vida máxima: "))

if tipo == "1":
    fuerza = int(input("Fuerza: "))
    personaje = Guerrero(nombre, vida, fuerza)
else:
    mana = int(input("Maná máximo: "))
    personaje = Mago(nombre, vida, mana)

# --- Lista fija de objetos (mínimo 4) ---
catalogo = [
    Arma("Espada larga", 12),
    Arma("Daga", 5),
    Usable("Poción menor", 15),
    Gema("Gema de fuego", "fuego"),
]

# --- Elegir objetos hasta terminar ---
while True:
    print("\nObjetos disponibles:")
    numero = 1
    for objeto in catalogo:
        print(f"{numero}. {objeto.describir()}")
        numero = numero + 1
    print("0. Terminar")

    opcion = int(input("Elige una opción: "))
    if opcion == 0:
        break
    personaje.inventario.agregar(catalogo[opcion - 1])

# --- Mostrar resultado ---
print("\n=== Tu personaje ===")
print("Nombre:", personaje.nombre)
print("Clase:", type(personaje).__name__)
print("Vida:", personaje.get_vida())
if tipo == "1":
    print("Fuerza:", personaje.fuerza)
else:
    print("Maná:", personaje.get_mana())

print("\n=== Mochila ===")
personaje.inventario.mostrar()