class Objeto:
    def __init__(self, nombre):
        self.nombre = nombre

    def describir(self):
        raise NotImplementedError("Cada objeto debe implementar describir()")


class Arma(Objeto):
    def __init__(self, nombre, daño):
        super().__init__(nombre)
        self.daño = daño

    def describir(self):
        return f"{self.nombre} (arma, +{self.daño} de daño)"


class Usable(Objeto):
    def __init__(self, nombre, curacion):
        super().__init__(nombre)
        self.curacion = curacion

    def describir(self):
        return f"{self.nombre} (usable, cura {self.curacion} de vida)"


class Gema(Objeto):
    def __init__(self, nombre, elemento):
        super().__init__(nombre)
        self.elemento = elemento

    def describir(self):
        return f"{self.nombre} (gema de {self.elemento})"


class Inventario:
    def __init__(self):
        self._objetos = []

    def agregar(self, objeto):
        self._objetos.append(objeto)

    def mostrar(self):
        for objeto in self._objetos:
            print(objeto.describir())