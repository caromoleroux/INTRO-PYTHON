class Persona:
    '''
    Crear los objetos de tipo Persona
    '''
    def __init__(self, nombre, genero, ocupacion=None, cedula=None): #metodo que inicializa al objeto de tipo persona (constructor)
        self._nombre = nombre
        self._genero = genero
        self._ocupacion = ocupacion
        self._cedula = cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor):
        self._genero = valor

    @property
    def ocupacion(self):
        return self._ocupacion

    @ocupacion.setter
    def ocupacion(self, valor):
        self._ocupacion = valor

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, valor):
        self._cedula = valor

    def __str__(self): #downders son sobre escritos
        return (f'Persona: [nombre: {self._nombre}, genero: {self._genero}, '
                f'ocupación: {self._ocupacion}, cédula: {self._cedula}]')

    def saludar(self):
        print(f'Hola soy {self._nombre}')


if __name__ == '__main__':
    obj_persona1 = Persona('Luis', 'M', 'Estudiante', '1234567890')
    print(obj_persona1.__str__())
    obj_persona2 = Persona(genero='F', ocupacion='Tecnolog', nombre='Maria', cedula='0987654321')
    print(obj_persona2)
    p3 = Persona(nombre='Jose', genero='M')
    print(p3)
    obj_persona1.saludar()
