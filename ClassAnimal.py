class Animal:
    # Constructor (__init__) para inicializar las propiedades
    def __init__(self, especie, color, genero):
        self.especie = especie
        self.color = color
        self.genero = genero

    # Método para mostrar la información del animal
    def mostrar_info(self):
        print(f"Especie: {self.especie}")
        print(f"Color: {self.color}")
        print(f"Genero: {self.genero}")

    # Método para comer com parametro
    def comer(self, tipoAlimento=""):
        if tipoAlimento == "":
            print(f"El animal de especie: {self.especie}, de color: {self.color} esta comiendo.")
        else:
            print(f"El animal de especie: {self.especie}, de color: {self.color} esta comiendo {tipoAlimento}.")

    # Método para comer com parametro
    def comer2(self, *args):
        if len(args) == 0:
            print(f"El animal de especie: {self.especie}, de color: {self.color} esta comiendo.")
        else:
            detalles = ", ".join(args)
            print(f"El animal de especie: {self.especie}, de color: {self.color} esta comiendo con el siguiente detalle: {detalles}.")
          
    # Método para correr el animal
    def correr(self):
        print(f"El animal de especie: {self.especie}, de color: {self.color} esta corriendo.")

# Crear objetos de la clase Animal
animal1 = Animal("gato", "negro", "macho")
animal2 = Animal("perro", "amarillo", "macho")

# Usar los métodos de los objetos
animal1.mostrar_info()
animal1.comer()
animal1.comer2()
animal1.correr()

print()  # Separador entre Animales

animal2.mostrar_info()
animal2.comer("alfalfa")
animal2.comer2("balanceado", "30% de proteinas", "2 pm")
animal2.correr()