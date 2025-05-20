from abc import ABC, abstractmethod

# Clase raíz
class Mascota(ABC):
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    @abstractmethod
    def sonido():
        pass


# Clase Perro
class Perro(Mascota):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color)
        self.peso = peso
        self.muerde = muerde

    @staticmethod
    def sonido():
        print("Los perros ladran")


class PerroPequeno(Perro): pass
class PerroMediano(Perro): pass
class PerroGrande(Perro): pass


# Clase Gato
class Gato(Mascota):
    def __init__(self, nombre, edad, color, altura_salto, longitud_salto):
        super().__init__(nombre, edad, color)
        self.altura_salto = altura_salto
        self.longitud_salto = longitud_salto

    @staticmethod
    def sonido():
        print("Los gatos maúllan y ronronean")


class GatoSinPelo(Gato): pass
class GatoPeloLargo(Gato): pass
class GatoPeloCorto(Gato): pass


# Diccionarios de razas
razas_perros = {
    "pequeno": ["caniche", "yorkshire terrier", "schnauzer", "chihuahua"],
    "mediano": ["collie", "dálmata", "bulldog", "galgo", "sabueso"],
    "grande": ["pastor alemán", "doberman", "rottweiler"]
}

razas_gatos = {
    "sin_pelo": ["esfinge", "elfo", "donskoy"],
    "pelo_largo": ["angora", "himalayo", "balinés", "somalí"],
    "pelo_corto": ["azul ruso", "británico", "manx", "devon rex"]
}


# Función para mostrar menú y devolver raza seleccionada
def elegir_raza(menu):
    opciones = []
    i = 1
    for grupo, lista in menu.items():
        print(f"\n{grupo.replace('_', ' ').capitalize()}:")
        for raza in lista:
            print(f"  {i}. {raza}")
            opciones.append((grupo, raza))
            i += 1
    while True:
        try:
            eleccion = int(input("\nElige el número de la raza: "))
            if 1 <= eleccion <= len(opciones):
                return opciones[eleccion - 1]
            else:
                print("Número fuera de rango.")
        except ValueError:
            print("Por favor ingresa un número válido.")


# Interacción principal
def main():
    tipo = input("¿Qué tipo de mascota es? (perro/gato): ").strip().lower()
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    color = input("Color: ")

    if tipo == "perro":
        print("\nSelecciona la raza del perro:")
        grupo, raza = elegir_raza(razas_perros)

        peso = float(input("Peso (kg): "))
        muerde = input("¿Muerde? (s/n): ").strip().lower() == "s"

        if grupo == "pequeno":
            mascota = PerroPequeno(nombre, edad, color, peso, muerde)
        elif grupo == "mediano":
            mascota = PerroMediano(nombre, edad, color, peso, muerde)
        elif grupo == "grande":
            mascota = PerroGrande(nombre, edad, color, peso, muerde)

    elif tipo == "gato":
        print("\nSelecciona la raza del gato:")
        grupo, raza = elegir_raza(razas_gatos)

        altura = float(input("Altura de salto (m): "))
        longitud = float(input("Longitud de salto (m): "))

        if grupo == "sin_pelo":
            mascota = GatoSinPelo(nombre, edad, color, altura, longitud)
        elif grupo == "pelo_largo":
            mascota = GatoPeloLargo(nombre, edad, color, altura, longitud)
        elif grupo == "pelo_corto":
            mascota = GatoPeloCorto(nombre, edad, color, altura, longitud)
    else:
        print("Tipo no válido. Debe ser 'perro' o 'gato'.")
        return

    print(f"\n✅ ¡Mascota registrada! {nombre} es un(a) {raza} de la clase: {mascota.__class__.__name__}")
    mascota.sonido()


if __name__ == "__main__":
    main()
