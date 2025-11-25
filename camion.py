class camion:
    
    def __init__(self, nombre, color, modelo, aceleracion, carga, placa):
        self.nombre = nombre
        self.color = color
        self.modelo = modelo
        self.aceleracion = aceleracion
        self.carga = carga
        self.placa = placa

    def funcion(self):
        print(f"el camion {self.nombre} obtiene una aceleracion de  {self.aceleracion}.")
        print(f"el camion {self.nombre} lleva una carga de  {self.carga}.")
        
camion1 = camion("dodge ","verde","1998","50 km/h","8000 kg","DOG546")           

print(f"El nombre de camion1 es: {camion1.nombre}")
print(f"El color de camion1 es: {camion1.color}")
print(f"El modelo de camion1 es: {camion1.modelo}")
print(f"La placa de camion1 es: {camion1.placa}")

camion1.funcion()

    