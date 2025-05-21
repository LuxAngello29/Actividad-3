# Clase base Profesor
class Profesor:
    def imprimir(self):
        print("Es un profesor.")

# Clase derivada ProfesorTitular que hereda de Profesor
class ProfesorTitular(Profesor):
    def imprimir(self):
        print("Es un profesor titular.")

# Clase Prueba (función main)
def main():
    # Primer caso del ejercicio
    profesor1 = ProfesorTitular()  
    profesor1.imprimir()           

    # Segundo caso propuesto
    profesor2 = ProfesorTitular()
    profesor2 = (profesor2)  
    profesor2.imprimir()    

if __name__ == "__main__":
    main()
