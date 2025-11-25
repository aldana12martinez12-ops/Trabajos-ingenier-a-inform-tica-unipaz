class ejercito:
    
    def __init__(self, rango, identificacion, Nombre, peloton):
        self.rango = rango
        self.identificacion = identificacion
        self.Nombre = Nombre
        self.peloton = peloton
             
class soldados_rasos(ejercito):
    def __init__(self, rango, identificacion, Nombre, peloton, alias, t_s_a_p):
        super().__init__(rango, identificacion, Nombre, peloton)
        self.alias = alias
        self.t_s_a_p = t_s_a_p
    def hablar_s(self):
        print(f"Hola soy {self.Nombre}, mi rango es {self.rango}, pertenezco al peloton {self.peloton}, mi alias es {self.alias} y mi tiempo de servicio a prestar es {self.t_s_a_p}.")
class cabo(ejercito):
    def __init__(self, rango, identificacion, Nombre, peloton, t_s_p):
        super().__init__(rango, identificacion, Nombre, peloton)
        self.t_s_p = t_s_p
    def hablar_c(self):
        print(f"Hola soy {self.Nombre}, mi rango es {self.rango}, pertenezco al peloton {self.peloton} y mi tiempo de servicio prestado es {self.t_s_p}.")
class sargento(ejercito):
    def __init__(self, rango, identificacion, Nombre, peloton, peloton_cargo):
        super().__init__(rango, identificacion, Nombre, peloton)
        self.peloton_cargo = peloton_cargo
    def hablar_S(self):
        print(f"Hola soy {self.Nombre}, mi rango es {self.rango}, pertenezco al peloton {self.peloton} y estoy a cargo del peloton  {self.peloton_cargo}.")    
class teniente(ejercito):
    def __init__(self, rango, identificacion, Nombre, peloton, n_o_a_c):
        super().__init__(rango, identificacion, Nombre, peloton)
        self.n_o_a_c = n_o_a_c
    def hablar_t(self):
        print(f"Hola soy {self.Nombre}, mi rango es {self.rango}, pertenezco al peloton {self.peloton} y estoy a cargo de {self.n_o_a_c} oficiales.")     
class general(ejercito):
    def __init__(self, rango, identificacion, Nombre, peloton, batallon):
        super().__init__(rango, identificacion, Nombre, peloton)
        self.batallon = batallon
    def hablar_g(self):
        print(f"Hola soy {self.Nombre}, mi rango es {self.rango}, pertenezco al peloton {self.peloton} y estoy a cargo del batallon {self.batallon}.") 
        
                  
soldado1 = soldados_rasos("soldado raso","1001","Juan","1","juancho","2 meses")    
soldado2 = cabo("cabo","1002","pedro","2","4 meses") 
soldado3 = sargento("sargento","1003","samuel","3","1 peloton") 
soldado4 = teniente("teniente","1004","Julian","4","50") 
soldado5 = general("general","1005","Anderson","5","15") 
   

soldado1.hablar_s() 
soldado2.hablar_c() 
soldado3.hablar_S() 
soldado4.hablar_t() 
soldado5.hablar_g()    