class Animal:
    # Constructor (__init__) para inicializar las propiedades
    def __init__(self, especie, color, genero):
        self.especie = especie
        self.color = color
        self.genero = genero

    # Método para mostrar la información del auto
    def mostrar_info(self):
        print(f"Especie: {self.especie}")
        print(f"Color: {self.color}")
        print(f"Genero: {self.genero}")

    # Método para arrancar el auto
    def comer(self):
        print(f"El animal de especie: {self.especie}, de color: {self.color} esta comiendo.")

    # Método para detener el auto
    def correr(self):
        print(f"El animal de especie: {self.especie}, de color: {self.color} esta corriendo.")

# Crear objetos de la clase Auto
animal1 = Animal("gato", "negro", "macho")
animal2 = Animal("perro", "amarillo", "macho")

# Usar los métodos de los objetos
animal1.mostrar_info()
animal1.comer()
animal1.correr()

print()  # Separador entre autos

animal2.mostrar_info()
animal2.comer()
animal2.correr()