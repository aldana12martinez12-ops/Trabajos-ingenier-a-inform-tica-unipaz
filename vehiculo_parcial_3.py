class vehiculos:
    
    def __init__(self, marca, modelo, año, velocidad_actual):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad_actual = velocidad_actual
             
class carro(vehiculos):
    def __init__(self, marca, modelo, año, velocidad_actual, num_puertas):
        super().__init__(marca, modelo, año, velocidad_actual)
        self.num_puertas = num_puertas
    def acelerar_c(self, cantidad):
        self.velocidad_actual += cantidad        
        print(f"el carro {self.modelo} tiene un aceleracion de {cantidad} km/h y su velocidad actual es de {self.velocidad_actual} km/h.")
    def frenar_c(self,cantidad):
        if self.velocidad_actual < cantidad:
            self.velocidad_actual = 0
            print(f"el carro {self.modelo} disminuye su velocidad {cantidad} km/h y su velocidad actual es de {self.velocidad_actual} km/h.")
        else:    
            self.velocidad_actual -= cantidad        
            print(f"el carro {self.modelo} disminuye su velocidad {cantidad} km/h y su velocidad actual es de {self.velocidad_actual} km/h.")
    def mostrar_info_c(self):
        print(f"la marca es {self.marca}")
        print(f"el modelo es {self.modelo}")
        print(f"el año es {self.año}")
        print(f"el numero de puertas es {self.velocidad_actual}")                
class moto(vehiculos):
    def __init__(self, marca, modelo, año, velocidad_actual, cilindraje):
        super().__init__(marca, modelo, año, velocidad_actual)
        self.cilindraje = cilindraje
    def acelerar_m(self,cantidad):
        self.velocidad_actual += cantidad        
        print(f"la moto {self.modelo} tiene un aceleracion de {cantidad} km/h y su velocidad actual es de {self.velocidad_actual} km/h.")
    def frenar_m(self,cantidad):
        if self.velocidad_actual < cantidad:
            self.velocidad_actual = 0
            print(f"la moto {self.modelo} disminuye su velocidad {cantidad} km/h y su velocidad actual es de {self.velocidad_actual} km/h.")    
        else:    
            self.velocidad_actual -= cantidad        
            print(f"la moto {self.modelo} disminuye su velocidad {cantidad} km/h y su velocidad actual es de {self.velocidad_actual} km/h.")
    def mostrar_info_m(self):
        print(f"la marca es {self.marca}")
        print(f"el modelo es {self.modelo}")
        print(f"el año es {self.año}")
        print(f"el cilindraje es {self.cilindraje}")   
class bicicleta(vehiculos):
    def __init__(self, marca, modelo, año, velocidad_actual, tipo):
        super().__init__(marca, modelo, año, velocidad_actual)
        self.tipo = tipo
    def acelerar_b(self,cantidad):
        self.velocidad_actual += cantidad        
        print(f"la bicicleta {self.modelo} tiene un aceleracion de {cantidad} km/h y su velocidad actual es de {self.velocidad_actual} km/h.")
    def frenar_b(self,cantidad):
        if self.velocidad_actual < cantidad:
            self.velocidad_actual = 0
            print(f"la bicicleta {self.modelo} disminuye su velocidad {cantidad} km/h y su velocidad actual es de {self.velocidad_actual} km/h.")
        else:    
            self.velocidad_actual -= cantidad        
            print(f"la bicicleta {self.modelo} disminuye su velocidad {cantidad} km/h y su velocidad actual es de {self.velocidad_actual} km/h.")
    def mostrar_info_b(self):
        print(f"la marca es {self.marca}")
        print(f"el modelo es {self.modelo}")
        print(f"el año es {self.año}")
        print(f"el tipo es {self.tipo}")   
        
carro1= carro("lamborghini","huracan","2026",200,"2")
carro2 = carro("ferrari","SF90","1990",180,"2")

moto1 = moto("Suzuki","AX4","2010",40,"110 cc")
moto2 = moto("Kawasaki","H2R","2024",10,"998 cc")

bicicleta1 = bicicleta("GW","Acrobat","2020",40,"montaña")
bicicleta2 = bicicleta("fitness","Orbea","2013",35,"Urbana")

while "true":
    print("informacion vehiculos")
    print("1.iniciar simulacion")
    print("2. informacion")
    print("3.salir")
    
    opc = input("elige una opccion de informacion: ")
    if opc == "1":
        carro1.acelerar_c(20)
        carro2.frenar_c(30)  
        carro1.frenar_c(40)
        moto1.acelerar_m(20)
        moto1.frenar_m(10)
        carro2.acelerar_c(100)
        moto2.acelerar_m(200)
        bicicleta1.acelerar_b(100)
        bicicleta2.frenar_b(10) 
    elif opc == "2":
        carro1.mostrar_info_c()
        carro2.mostrar_info_c()
        moto1.mostrar_info_m()
        moto2.mostrar_info_m()
        bicicleta1.mostrar_info_b()
        bicicleta2.mostrar_info_b()      
    elif opc == "3":
        break
    else:
        print("error")                      