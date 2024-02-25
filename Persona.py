class Persona:
    '''
    Crear los objetos de tipo Persona
    '''
    def __init__(self, nombre, genero, ocupacion=None): #metodo que inicializa al objeto de tipo persona (constructor)
        self._nombre = nombre
        self._genero = genero
        self._ocupacion = ocupacion

    def __str__(self): #downders son sobre escritos
        return (f'Persona: [nombre: {self._nombre}, genero: {self._genero}, '
                f'ocupación: {self._ocupacion}]')

    def saludar(self):
        print(f'Hola soy {self._nombre}')


if __name__ == '__main__':
    obj_persona1 = Persona('Luis', 'M', 'Estudiante')
    print(obj_persona1.__str__())
    obj_persona2 = Persona(genero='F', ocupacion='Tecnolog', nombre='Maria')
    print(obj_persona2)
    p3 = Persona(nombre='Jose', genero='M')
    print(p3)
    obj_persona1.saludar()