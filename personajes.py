from abc import ABC, abstractmethod
from objetos import Inventario


class Personaje(ABC):
    def __init__(self, nombre, vida_maxima):
        self.nombre = nombre
        self.vida_maxima = vida_maxima
        self.set_vida(vida_maxima)
        self.inventario = Inventario()   # cada personaje nace con su mochila vacía

    def set_vida(self, valor):
        if valor < 0:
            valor = 0
        if valor > self.vida_maxima:
            valor = self.vida_maxima
        self._vida = valor

    def get_vida(self):
        return self._vida

    def recibir_daño(self, cantidad):
        self.set_vida(self._vida - cantidad)

    @abstractmethod
    def atacar(self):
        ...


class Guerrero(Personaje):
    def __init__(self, nombre, vida_maxima, fuerza):
        super().__init__(nombre, vida_maxima)
        self.fuerza = fuerza

    def atacar(self):
        return f"{self.nombre} da un espadazo por {self.fuerza} de daño"


class Mago(Personaje):
    def __init__(self, nombre, vida_maxima, mana_maxima):
        super().__init__(nombre, vida_maxima)
        self.mana_maxima = mana_maxima
        self.set_mana(mana_maxima)

    def set_mana(self, valor):
        if valor < 0:
            valor = 0
        self._mana = valor

    def get_mana(self):
        return self._mana

    def atacar(self):
        if self._mana < 5:
            return f"{self.nombre} no tiene maná para conjurar"
        self.set_mana(self._mana - 5)
        return f"{self.nombre} lanza una bola de fuego (maná restante: {self._mana})"