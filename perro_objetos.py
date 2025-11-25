class perro:
    
    def __init__(self, nombre, color, genero):
        self.nombre = nombre
        self.color = color
        self.genero = genero

    def ladrar(self):
        print(f"{self.nombre} dice: wof! soy de color {self.color}.")
        
perro1 = perro("Coco","negro","macho")           
perro2 = perro("Kiriku","cafe","macho")
perro3 = perro("Candy","blanca","hembra")

print(f"el nombre de perro1 es: {perro1.nombre}")
print(f"el color de perro2 es: {perro2.color}")
print(f"el genero de perro3 es: {perro3.genero}")

perro1.ladrar()
perro2.ladrar()
perro3.ladrar()
             
class perroDomestico(perro):
    def __init__(self, nombre, color, genero, lugar_favorito):
        super().__init__(nombre, color, genero)
        self.lugar_favorito = lugar_favorito
    def dormir_sofa(self):
           print(f"{self.nombre} esta durmiendo en su lugar favorito {self.lugar_favorito}.")
perro_hogar = perroDomestico("Garfield","Naranja","masculino","sofa")
perro_hogar.ladrar()
perro_hogar.dormir_sofa()           