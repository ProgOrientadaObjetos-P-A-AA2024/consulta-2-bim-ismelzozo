from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, nombre):
        self._nombre_figura = nombre

    def establecer_nombre_figura(self, nombre):
        self._nombre_figura = nombre

    def obtener_nombre_figura(self):
        return self._nombre_figura

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def obtener_area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, nombre, lado):
        super().__init__(nombre)
        self._lado = lado
        self._area = 0.0

    def establecer_lado(self, lado):
        self._lado = lado

    def obtener_lado(self):
        return self._lado

    def calcular_area(self):
        self._area = self._lado * self._lado

    def obtener_area(self):
        return self._area

class Triangulo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self._base = base
        self._altura = altura
        self._area = 0.0

    def establecer_base(self, base):
        self._base = base

    def obtener_base(self):
        return self._base

    def establecer_altura(self, altura):
        self._altura = altura

    def obtener_altura(self):
        return self._altura

    def calcular_area(self):
        self._area = (self._base * self._altura) / 2

    def obtener_area(self):
        return self._area


class Rombo(Figura):
    def __init__(self, nombre, diagonal_mayor, diagonal_menor):
        super().__init__(nombre)
        self._diagonal_mayor = diagonal_mayor
        self._diagonal_menor = diagonal_menor
        self._area = 0.0

    def establecer_diagonal_mayor(self, diagonal_mayor):
        self._diagonal_mayor = diagonal_mayor

    def obtener_diagonal_mayor(self):
        return self._diagonal_mayor

    def establecer_diagonal_menor(self, diagonal_menor):
        self._diagonal_menor = diagonal_menor

    def obtener_diagonal_menor(self):
        return self._diagonal_menor

    def calcular_area(self):
        self._area = (self._diagonal_mayor * self._diagonal_menor) / 2

    def obtener_area(self):
        return self._area


def main():
    # Ejemplo de polimorfismo
    f1 = Cuadrado("Cuadrado", 4)
    f1.calcular_area()

    f2 = Triangulo("Triángulo", 4, 6)
    f2.calcular_area()

    f3 = Rombo("Rombo", 8, 6)
    f3.calcular_area()

    print(f"Figura 1: {f1.obtener_nombre_figura()} - Área: {f1.obtener_area():.2f}")
    print(f"Figura 2: {f2.obtener_nombre_figura()} - Área: {f2.obtener_area():.2f}")
    print(f"Figura 3: {f3.obtener_nombre_figura()} - Área: {f3.obtener_area():.2f}")


if __name__ == "__main__":
    main()