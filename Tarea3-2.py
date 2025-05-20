from enum import Enum

class TipoLocal(Enum):
    INTERNO = "INTERNO"
    CALLE = "CALLE"

class Inmueble:
    def __init__(self, identificador, area, direccion):
        self._id = identificador
        self._area = area
        self._direccion = direccion
        self._precio_venta = 0

    def calcular_precio_venta(self, valor_m2):
        self._precio_venta = self._area * valor_m2

    def imprimir(self):
        print(f"Identificador = {self._id}")
        print(f"Área = {self._area}")
        print(f"Dirección = {self._direccion}")
        print(f"Precio de venta = ${self._precio_venta:,.2f}")

class InmuebleVivienda(Inmueble):
    def __init__(self, identificador, area, direccion, habitaciones, banos):
        super().__init__(identificador, area, direccion)
        self._hab = habitaciones
        self._banos = banos

    def imprimir(self):
        super().imprimir()
        print(f"Habitaciones = {self._hab}")
        print(f"Baños = {self._banos}")

class Casa(InmuebleVivienda):
    def __init__(self, identificador, area, direccion, hab, banos, pisos):
        super().__init__(identificador, area, direccion, hab, banos)
        self._pisos = pisos

    def imprimir(self):
        super().imprimir()
        print(f"Pisos = {self._pisos}")

class CasaRural(Casa):
    def __init__(self, *args, distancia, altitud):
        super().__init__(*args)
        self._distancia = distancia
        self._altitud = altitud
        self.calcular_precio_venta(1_500_000)
    def imprimir(self):
        print("=== Casa Rural ===")
        super().imprimir()
        print(f"Distancia a cabecera = {self._distancia} km")
        print(f"Altitud = {self._altitud} m")

class CasaConjuntoCerrado(Casa):
    def __init__(self, *args, valor_admin, piscina, campos):
        super().__init__(*args)
        self._valor_admin = valor_admin
        self._piscina = piscina
        self._campos = campos
        self.calcular_precio_venta(2_500_000)
    def imprimir(self):
        print("=== Casa en Conjunto Cerrado ===")
        super().imprimir()
        print(f"Valor administración = ${self._valor_admin:,.2f}")
        print(f"Tiene piscina = {self._piscina}")
        print(f"Tiene campos deportivos = {self._campos}")

class CasaIndependiente(Casa):
    def __init__(self, *args):
        super().__init__(*args)
        self.calcular_precio_venta(3_000_000)
    def imprimir(self):
        print("=== Casa Independiente ===")
        super().imprimir()

class Apartamento(InmuebleVivienda):
    pass

class ApartamentoFamiliar(Apartamento):
    def __init__(self, *args, valor_admin):
        super().__init__(*args)
        self._valor_admin = valor_admin
        self.calcular_precio_venta(2_000_000)
    def imprimir(self):
        print("=== Apartamento Familiar ===")
        super().imprimir()
        print(f"Valor administración = ${self._valor_admin:,.2f}")

class Apartaestudio(Apartamento):
    def __init__(self, *args):
        super().__init__(*args)
        self.calcular_precio_venta(1_500_000)
    def imprimir(self):
        print("=== Apartaestudio ===")
        super().imprimir()

class Local(Inmueble):
    def __init__(self, *args, tipo: TipoLocal):
        super().__init__(*args)
        self._tipo = tipo
    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local = {self._tipo.value}")

class LocalComercial(Local):
    def __init__(self, *args, centro):
        super().__init__(*args)
        self._centro = centro
        self.calcular_precio_venta(3_000_000)
    def imprimir(self):
        print("=== Local Comercial ===")
        super().imprimir()
        print(f"Centro comercial = {self._centro}")

class Oficina(Local):
    def __init__(self, *args, es_gobierno):
        super().__init__(*args)
        self._es_gobierno = es_gobierno
        self.calcular_precio_venta(3_500_000)
    def imprimir(self):
        print("=== Oficina ===")
        super().imprimir()
        print(f"Es del gobierno = {self._es_gobierno}")

def crear_inmueble():
    print("¿Qué tipo de inmueble deseas registrar?")
    print("1) Vivienda")
    print("2) Local")
    tipo = input("Elige 1 o 2: ").strip()

    id_ = int(input("Identificador inmobiliario: "))
    area = int(input("Área (m²): "))
    direccion = input("Dirección: ")

    if tipo == "1":
        # Vivienda
        hab = int(input("Número de habitaciones: "))
        banos = int(input("Número de baños: "))
        print("¿Es casa o apartamento? (c/a)")
        sub = input().lower()

        if sub == "c":
            pisos = int(input("Número de pisos: "))
            print("¿Qué tipo de casa? 1) Rural  2) Conjunto  3) Independiente")
            opc = input("Elige 1,2 o 3: ").strip()
            if opc == "1":
                dist = int(input("Distancia a cabecera (km): "))
                alt = int(input("Altitud (m): "))
                return CasaRural(id_, area, direccion, hab, banos, pisos, distancia=dist, altitud=alt)
            elif opc == "2":
                val = float(input("Valor de administración: "))
                piscina = input("¿Tiene piscina? (s/n): ").lower() == "s"
                campos = input("¿Tiene campos deportivos? (s/n): ").lower() == "s"
                return CasaConjuntoCerrado(id_, area, direccion, hab, banos, pisos,
                                           valor_admin=val, piscina=piscina, campos=campos)
            else:
                return CasaIndependiente(id_, area, direccion, hab, banos, pisos)

        else:
            # Apartamento
            print("¿Qué tipo de apartamento? 1) Familiar  2) Estudio")
            opc = input("Elige 1 o 2: ").strip()
            if opc == "1":
                val = float(input("Valor de administración: "))
                return ApartamentoFamiliar(id_, area, direccion, hab, banos, valor_admin=val)
            else:
                return Apartaestudio(id_, area, direccion, hab, banos)

    else:
        # Local
        print("¿Tipo de local? 1) Interno  2) Calle")
        t = input("Elige 1 o 2: ").strip()
        tipo_local = TipoLocal.INTERNO if t == "1" else TipoLocal.CALLE
        print("¿Es 1) Comercial  o  2) Oficina?")
        opc = input("Elige 1 o 2: ").strip()
        if opc == "1":
            centro = input("Centro comercial: ")
            return LocalComercial(id_, area, direccion, tipo=tipo_local, centro=centro)
        else:
            esg = input("¿Es del gobierno? (s/n): ").lower() == "s"
            return Oficina(id_, area, direccion, tipo=tipo_local, es_gobierno=esg)

if __name__ == "__main__":
    inmueble = crear_inmueble()
    print("\n--- Datos registrados ---")
    inmueble.imprimir()

