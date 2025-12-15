class Vehiculo:
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.numero_puertas = numero_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible

    def arranque(self):
        return "El vehículo ha arrancado."

    def apagado(self):
        return "El vehículo está apagado."

    def aceleracion_frenado(self):
        return "Puede acelerar y frenar normalmente."

    def sistema_direccion(self):
        return "Cuenta con dirección estándar."

    def climatizacion(self):
        return "Sistema de aire acondicionado básico."
