class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamano = tamano
        self.color = color

    def moverse(self):
        return "El animal se está moviendo."

    def comunicacion(self):
        return "El animal se comunica."

    def alimentarse(self):
        return "El animal se está alimentando."

    def adaptacion(self):
        return "El animal se adapta a su entorno."

    def dormir(self):
        return "El animal está durmiendo."
