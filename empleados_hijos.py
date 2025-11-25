class empleado:
    
    def __init__(self, Identificacion, Rol, Nombre):
        self.Identificacion = Identificacion
        self.Rol = Rol
        self.Nombre = Nombre
             
class gerente(empleado):
    def __init__(self, Identificacion, Rol, Nombre, Salario):
        super().__init__(Identificacion, Rol, Nombre)
        self.Salario = Salario
    def hablar_G(self):
        print(f"Hola soy {self.Nombre} y mi rol es {self.Rol} y mi salario es {self.Salario}.")
class empleado_ordinario(empleado):
    def __init__(self, Identificacion, Rol, Nombre, Salario, horas_trabajo):
        super().__init__(Identificacion, Rol, Nombre)
        self.Salario = Salario
        self.horas_trabajo = horas_trabajo
    def hablar_e(self):
        print(f"Hola soy {self.Nombre} y mi rol es {self.Rol} y mi salario es {self.Salario} con {self.horas_trabajo} a la semana.")                
        
empleado1 = gerente("10","Gerente","Luis","3 SMLV")    
empleado2 = empleado_ordinario("11","empleado ordinario","Camilo","2 SMLV","40 h")
empleado3 = gerente("12","Gerente","Sofia","3 SMLV")

print(f"el ID de empleado1 es: {empleado1.Identificacion}")
print(f"el ID de empleado2 es: {empleado2.Identificacion}")
print(f"el ID de empleado3 es: {empleado3.Identificacion}")     

empleado1.hablar_G() 
empleado2.hablar_e() 
empleado3.hablar_G()   
  