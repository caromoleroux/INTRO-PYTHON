class Persona:
    '''
    Crear los objetos de tipo Persona
    '''
    def __init__(self, nombre, genero, ocupacion=None):
        self._nombre = nombre
        self._genero = genero
        self._ocupacion = ocupacion

    def __str__(self):
        return (f'Persona: [nombre: {self._nombre}, genero: {self._genero}, '
                f'ocupación: {self._ocupacion}]')

    def saludar(self):
        print(f'Hola soy {self._nombre}')

class Cliente(Persona):
    '''
    Crear los objetos de tipo Cliente, hereda de Persona
    '''
    def __init__(self, nombre, genero, ocupacion=None, email=None):
        super().__init__(nombre, genero, ocupacion)
        self._email = email

    def __str__(self):
        return (f'Cliente: [nombre: {self._nombre}, genero: {self._genero}, '
                f'ocupación: {self._ocupacion}, email: {self._email}]')

# Ejemplo de uso
if __name__ == '__main__':
    cliente1 = Cliente('Luis', 'M', 'Estudiante', 'luis@gmail.com')
    print(cliente1)
    cliente2 = Cliente('Maria', 'F', email='maria@gmail.com')
    print(cliente2)
    cliente3 = Cliente('Jose', 'M')
    print(cliente3)
    cliente1.saludar()
