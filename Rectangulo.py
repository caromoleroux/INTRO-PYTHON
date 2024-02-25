from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def __str__(self):
        return f"Rectangulo: Alto={self.alto}, Ancho={self.ancho}, Color={self.color}"

# Ejemplo de uso
rectangulo = Rectangulo(5, 10, "rojo")
print(rectangulo)  # Output: Rectangulo: Alto=5, Ancho=10, Color=rojo

# Modificando el alto, ancho y color
rectangulo.alto = 8
rectangulo.ancho = 15
rectangulo.color = "azul"
print(rectangulo)  # Output: Rectangulo: Alto=8, Ancho=15, Color=azul