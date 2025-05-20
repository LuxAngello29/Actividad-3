class Persona:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    def getNombre(self):
        return self.nombre

    def getDireccion(self):
        return self.direccion

    def setNombre(self, nombre):
        self.nombre = nombre

    def setDireccion(self, direccion):
        self.direccion = direccion


class Estudiante(Persona):
    def __init__(self, nombre, direccion, carrera, semestre):
        super().__init__(nombre, direccion)
        self.carrera = carrera
        self.semestre = semestre

    def getCarrera(self):
        return self.carrera

    def getSemestre(self):
        return self.semestre

    def setCarrera(self, carrera):
        self.carrera = carrera

    def setSemestre(self, semestre):
        self.semestre = semestre

    def resumen(self):
        return f"Estudiante: {self.nombre}, Dirección: {self.direccion}, Carrera: {self.carrera}, Semestre: {self.semestre}"


class Profesor(Persona):
    def __init__(self, nombre, direccion, departamento, categoria):
        super().__init__(nombre, direccion)
        self.departamento = departamento
        self.categoria = categoria

    def getDepartamento(self):
        return self.departamento

    def getCategoria(self):
        return self.categoria

    def setDepartamento(self, departamento):
        self.departamento = departamento

    def setCategoria(self, categoria):
        self.categoria = categoria

    def resumen(self):
        return f"Profesor: {self.nombre}, Dirección: {self.direccion}, Departamento: {self.departamento}, Categoría: {self.categoria}"


# Función principal para ingresar datos
def main():
    print("¿Deseas ingresar un Estudiante o un Profesor?")
    tipo = input("Escribe 'E' para Estudiante o 'P' para Profesor: ").strip().upper()

    nombre = input("Nombre: ")
    direccion = input("Dirección: ")

    if tipo == 'E':
        carrera = input("Carrera: ")
        semestre = int(input("Semestre: "))
        estudiante = Estudiante(nombre, direccion, carrera, semestre)
        print("\nClase detectada: Estudiante")
        print(estudiante.resumen())
    elif tipo == 'P':
        departamento = input("Departamento: ")
        categoria = input("Categoría: ")
        profesor = Profesor(nombre, direccion, departamento, categoria)
        print("\nClase detectada: Profesor")
        print(profesor.resumen())
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
