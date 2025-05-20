class Cuenta:
    def __init__(self, saldo: float, tasa_anual: float):
        self._saldo = saldo
        self._num_consignaciones = 0
        self._num_retiros = 0
        self._tasa_anual = tasa_anual
        self._comision_mensual = 0.0

    def consignar(self, cantidad: float):
        if cantidad > 0:
            self._saldo += cantidad
            self._num_consignaciones += 1

    def retirar(self, cantidad: float):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            self._num_retiros += 1
        else:
            print("La cantidad a retirar excede el saldo actual.")

    def calcular_interes_mensual(self):
        interes_mensual = (self._tasa_anual / 12) / 100 * self._saldo
        self._saldo += interes_mensual

    def extracto_mensual(self):
        self._saldo -= self._comision_mensual
        self.calcular_interes_mensual()

    def imprimir(self):
        print(f"Saldo: ${self._saldo:.2f}")
        print(f"Consignaciones: {self._num_consignaciones}")
        print(f"Retiros: {self._num_retiros}")
        print(f"Tasa anual: {self._tasa_anual}%")
        print(f"Comisión mensual: ${self._comision_mensual:.2f}")


class CuentaAhorros(Cuenta):
    def __init__(self, saldo: float, tasa_anual: float):
        super().__init__(saldo, tasa_anual)
        self._activa = self._saldo >= 10000

    def actualizar_estado(self):
        self._activa = self._saldo >= 10000

    def consignar(self, cantidad: float):
        self.actualizar_estado()
        if self._activa:
            super().consignar(cantidad)

    def retirar(self, cantidad: float):
        self.actualizar_estado()
        if self._activa and cantidad <= self._saldo:
            super().retirar(cantidad)
        else:
            print("Cuenta inactiva o saldo insuficiente.")

    def extracto_mensual(self):
        exceso_retiros = max(0, self._num_retiros - 4)
        self._comision_mensual = exceso_retiros * 1000
        super().extracto_mensual()
        self.actualizar_estado()

    def imprimir(self):
        transacciones = self._num_consignaciones + self._num_retiros
        print("=== Cuenta de Ahorros ===")
        print(f"Estado: {'Activa' if self._activa else 'Inactiva'}")
        print(f"Saldo: ${self._saldo:.2f}")
        print(f"Comisión mensual: ${self._comision_mensual:.2f}")
        print(f"Número de transacciones: {transacciones}")


class CuentaCorriente(Cuenta):
    def __init__(self, saldo: float, tasa_anual: float):
        super().__init__(saldo, tasa_anual)
        self._sobregiro = 0.0

    def retirar(self, cantidad: float):
        resultado = self._saldo - cantidad
        if resultado < 0:
            self._sobregiro -= resultado
            self._saldo = 0
        else:
            self._saldo = resultado
        self._num_retiros += 1

    def consignar(self, cantidad: float):
        if self._sobregiro > 0:
            if cantidad > self._sobregiro:
                restante = cantidad - self._sobregiro
                self._sobregiro = 0
                self._saldo += restante
            else:
                self._sobregiro -= cantidad
        else:
            self._saldo += cantidad
        self._num_consignaciones += 1

    def extracto_mensual(self):
        super().extracto_mensual()

    def imprimir(self):
        transacciones = self._num_consignaciones + self._num_retiros
        print("=== Cuenta Corriente ===")
        print(f"Saldo: ${self._saldo:.2f}")
        print(f"Comisión mensual: ${self._comision_mensual:.2f}")
        print(f"Número de transacciones: {transacciones}")
        print(f"Valor de sobregiro: ${self._sobregiro:.2f}")


# Función principal que selecciona tipo de cuenta automáticamente
def main():
    print("Bienvenido al sistema bancario")

    saldo = float(input("Ingrese el saldo inicial: $"))
    tasa = float(input("Ingrese la tasa de interés anual (%): "))
    tipo = input("¿Desea permitir sobregiro? (s/n): ").strip().lower()

    if tipo == 's':
        cuenta = CuentaCorriente(saldo, tasa)
    else:
        cuenta = CuentaAhorros(saldo, tasa)

    cantidad_deposito = float(input("Ingrese cantidad a consignar: $"))
    cuenta.consignar(cantidad_deposito)

    cantidad_retiro = float(input("Ingrese cantidad a retirar: $"))
    cuenta.retirar(cantidad_retiro)

    cuenta.extracto_mensual()
    cuenta.imprimir()


if __name__ == "__main__":
    main()
