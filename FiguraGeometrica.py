class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor > 0:
            self._alto = valor
        else:
            print("El valor del alto debe ser mayor que cero.")

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor > 0:
            self._ancho = valor
        else:
            print("El valor del ancho debe ser mayor que cero.")

    def __str__(self):
        return f"FiguraGeometrica: Alto={self.alto}, Ancho={self.ancho}"


# Ejemplo de uso
figura = FiguraGeometrica(5, 10)
print(figura)  # Output: FiguraGeometrica: Alto=5, Ancho=10

# Modificando el alto y ancho usando los setters
figura.alto = 8
figura.ancho = 15
print(figura)  # Output: FiguraGeometrica: Alto=8, Ancho=15
