class personaje:
    
    def __init__(self, nombre, color_ojos, color_pelo, genero, estatura, peso, raza, habilidades, edad, equipo_especial, vidas, resistencia, oficio, poder_de_equipo, tipo_de_arma, daño, nivel_del_arma):
        
        self.nombre = nombre
        self.color_ojos = color_ojos
        self.color_pelo = color_pelo
        self.genero = genero
        self.estatura = estatura
        self.peso = peso
        self.raza = raza
        self.habilidades = habilidades
        self.edad = edad
        self.equipo_especial = equipo_especial
        self.vidas = vidas
        self.resistencia= resistencia 
        self.oficio = oficio
        self.poder_de_equipo = poder_de_equipo
        self.tipo_de_arma = tipo_de_arma
        self.daño = daño
        self.nivel_del_arma= nivel_del_arma

    def hablar(self):
        print(f"soy {self.nombre} tengo {self.edad} años")
        print(f"y soy {self.raza} de tipo {self.habilidades}.")
        
        
personaje1 = personaje("Sung","azules","negro","masculino","180 cm","70 kg","mago","nigromante","18","armadura","3","500.000","cuidar a su familia","500.000","espadas","700.000","divino")    

personaje2= personaje("Sasha","claros","negro","femenino","168 cm","60 kg","curandera","curacion instantania","18","capa","3","50.000","cuidar a Sung","50.000","esferas","100.000","divino")              

print(f"El nombre de personaje1 es: {personaje1.nombre}")
print(f"El color de ojos {personaje1.nombre} es: {personaje1.color_ojos}")
print(f"El genero de {personaje1.nombre} es: {personaje1.genero}")
print(f"El color de pelo de {personaje1.nombre} es: {personaje1.color_pelo}")
print(f"La estatura de {personaje1.nombre} es: {personaje1.estatura}")
print(f"El peso de {personaje1.nombre} es: {personaje1.peso}")
print(f"La edad de {personaje1.nombre} es: {personaje1.edad}")

personaje1.hablar()

    