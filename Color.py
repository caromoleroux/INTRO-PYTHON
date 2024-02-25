class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, nuevo_color):
        self._color = nuevo_color

    def __str__(self):
        return f"Color: {self.color}"


# Ejemplo de uso
color_obj = Color("rojo")
print(color_obj)  # Output: Color: rojo

# Modificando el color
color_obj.color = "azul"
print(color_obj)  # Output: Color: azul
