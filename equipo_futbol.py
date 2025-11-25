class equipo:
    
    def __init__(self, posicion, dorsal, Nombre, goles_marcados):
        self.posicion = posicion
        self.dorsal = dorsal
        self.Nombre = Nombre
        self.goles_marcados = goles_marcados    
class arquero(equipo):
    def __init__(self, posicion, dorsal, Nombre, goles_marcados, cuantos_goles_tapo):
        super().__init__(posicion, dorsal, Nombre, goles_marcados)
        self.cuantos_goles_tapo = cuantos_goles_tapo
    def hablar_a(self):
        print(f"yo {self.goles_marcados}")
class lateral1(equipo):
    def __init__(self, posicion, dorsal, Nombre, goles_marcados, cuantos_jugadores_bloqueo):
        super().__init__(posicion, dorsal, Nombre, goles_marcados)
        self.cuantos_jugadores_bloqueo = cuantos_jugadores_bloqueo
    def hablar_l1(self):
        print(f"")
class lateral2(equipo):
    def __init__(self, posicion, dorsal, Nombre, goles_marcados, cuantos_jugadores_bloqueo):
        super().__init__(posicion, dorsal, Nombre, goles_marcados)
        self.cuantos_jugadores_bloqueo = cuantos_jugadores_bloqueo
    def hablar_l2(self):
        print(f"")
class armador(equipo):
    def __init__(self, posicion, dorsal, Nombre, goles_marcados, cuantas_jugadas_realizo):
        super().__init__(posicion, dorsal, Nombre, goles_marcados)
        self.cuantas_jugadas_realizo = cuantas_jugadas_realizo
    def hablar_ar(self):
        print(f"")
class delantero(equipo):
    def __init__(self, posicion, dorsal, Nombre, goles_marcados, cuantos_tiros_arco):
        super().__init__(posicion, dorsal, Nombre, goles_marcados)
        self.cuantos_tiros_arco = cuantos_tiros_arco
    def hablar_d(self):
        print(f"")
                

def mostrar_menu():
    print("Menu principal")
    print("1. iniciar partido")
    print("2. cerrar")
    

a1_1=0
l1_1=0
l2_1=0
ar_1=0
d_1=0

a1_2=0
l1_2=0
l2_2=0
ar_2=0
d_2=0
jugador1_equipo1 = arquero("Arquero","1","Samuel",a1_1,"11")
jugador2_equipo1 = lateral1("lateral izquierda","3","Pablo",l1_1,"2")
jugador3_equipo1 = lateral2("Lateral derecho","4","Mateo",l2_1,"3")
jugador4_equipo1 = armador("Armador","8","Pedri",ar_1,"25")
jugador5_equipo1 = delantero("delantero","11","Aldana",d_1,"11")
jugador1_equipo2 = arquero("Arquero","1","Santiago",a1_2,"11")
jugador2_equipo2 = lateral1("lateral izquierda","3","Pedro",l1_2,"2")
jugador3_equipo2 = lateral2("Lateral derecho","4","Marcos",l2_2,"3")
jugador4_equipo2 = armador("Armador","8","valverde",ar_2,"25")
jugador5_equipo2 = delantero("delantero","11","carlos",d_2,"11")

while 'true':
    mostrar_menu()  
    opc0 = input("Seleccione una opcion: ") 
        
    if opc0 == "1":
        while 'true':
            print("1.equipo 1")
            print("2.equipo 2")
            print("3. Acabar partido")
            
            opc = input("Seleccione una para marcar: ") 
             
            if opc == '1' :
                
                print("Elige jugador")
                print("1.Aquero")
                print("2.lateral 1")
                print("3.lteral 2")
                print("4.Armador")
                print("5.Delantero")
                
                opc2 = input("selecciona un jugador: ")
                
                if opc2 == "1":
                    a1_1 += 1
                    jugador1_equipo1 = arquero("Arquero","1","Samuel",a1_1,"11")
                    print(f"el arquero {jugador1_equipo1.Nombre} a marcado {jugador1_equipo1.goles_marcados} goles")
                if opc2 == "2":
                    l1_1 += 1
                    jugador2_equipo1 = lateral1("lateral izquierda","3","Pablo",l1_1,"2")
                    print(f"el lateral1 {jugador2_equipo1.Nombre} a marcado {jugador2_equipo1.goles_marcados} goles")           
                if opc2 == "3":
                    l2_1 += 1
                    jugador3_equipo1 = lateral2("Lateral derecho","4","Mateo",l2_1,"3")
                    print(f"el arquero {jugador3_equipo1.Nombre} a marcado {jugador3_equipo1.goles_marcados} goles")    
                if opc2 == "4":
                    ar_1 += 1
                    jugador4_equipo1 = armador("Armador","8","Pedri",ar_1,"25")
                    print(f"el arquero {jugador4_equipo1.Nombre} a marcado {jugador4_equipo1.goles_marcados} goles")   
                if opc2 == "5":
                    d_1 += 1
                    jugador5_equipo1 = delantero("delantero","11","Aldana",d_1,"11")
                    print(f"el arquero {jugador5_equipo1.Nombre} a marcado {jugador5_equipo1.goles_marcados} goles")
                                          
            elif opc == "2":
                                        
                print("Elige jugador")
                print("1.Aquero")
                print("2.lateral 1")
                print("3.lteral 2")
                print("4.Armador")
                print("5.Delantero")
                
                opc2 = input("selecciona un jugador: ")
                
                if opc2 == "1":
                    a1_2 += 1
                    jugador1_equipo2 = arquero("Arquero","1","Santiago",a1_2,"11")
                    print(f"el arquero {jugador1_equipo2.Nombre} a marcado {jugador1_equipo2.goles_marcados} goles")
                if opc2 == "2":
                    l1_2 += 1
                    jugador2_equipo2 = lateral1("lateral izquierda","3","Pedro",l1_2,"2")
                    print(f"el lateral1 {jugador2_equipo2.Nombre} a marcado {jugador2_equipo2.goles_marcados} goles")           
                if opc2 == "3":
                    l2_2 += 1
                    jugador3_equipo2 = lateral2("Lateral derecho","4","Marcos",l2_2,"3")
                    print(f"el arquero {jugador3_equipo2.Nombre} a marcado {jugador3_equipo2.goles_marcados} goles")    
                if opc2 == "4":
                    ar_2 += 1
                    jugador4_equipo2 = armador("Armador","8","valverde",ar_2,"25")
                    print(f"el arquero {jugador4_equipo2.Nombre} a marcado {jugador4_equipo2.goles_marcados} goles")   
                if opc2 == "5":
                    d_2 += 1
                    jugador5_equipo2 = delantero("delantero","11","carlos",d_2,"11")
                    print(f"el arquero {jugador5_equipo2.Nombre} a marcado {jugador5_equipo2.goles_marcados} goles")                 
            elif opc == "3" :
                print("equipo 1")
                print(f"el jugador {jugador1_equipo1.Nombre} del dorsal {jugador1_equipo1.dorsal} marco {jugador1_equipo1.goles_marcados} goles")
                print(f"el jugador {jugador2_equipo1.Nombre} del dorsal {jugador2_equipo1.dorsal} marco {jugador2_equipo1.goles_marcados} goles")
                print(f"el jugador {jugador3_equipo1.Nombre} del dorsal {jugador3_equipo1.dorsal} marco {jugador3_equipo1.goles_marcados} goles")
                print(f"el jugador {jugador4_equipo1.Nombre} del dorsal {jugador4_equipo1.dorsal} marco {jugador4_equipo1.goles_marcados} goles")
                print(f"el jugador {jugador5_equipo1.Nombre} del dorsal {jugador5_equipo1.dorsal} marco {jugador5_equipo1.goles_marcados} goles")
                print("equipo 2")
                print(f"el jugador {jugador1_equipo2.Nombre} del dorsal {jugador1_equipo2.dorsal} marco {jugador1_equipo2.goles_marcados} goles")
                print(f"el jugador {jugador2_equipo2.Nombre} del dorsal {jugador2_equipo2.dorsal} marco {jugador2_equipo2.goles_marcados} goles")
                print(f"el jugador {jugador3_equipo2.Nombre} del dorsal {jugador3_equipo2.dorsal} marco {jugador3_equipo2.goles_marcados} goles")
                print(f"el jugador {jugador4_equipo2.Nombre} del dorsal {jugador4_equipo2.dorsal} marco {jugador4_equipo2.goles_marcados} goles")
                print(f"el jugador {jugador5_equipo2.Nombre} del dorsal {jugador5_equipo2.dorsal} marco {jugador5_equipo2.goles_marcados} goles")                                                                                                                                                
                break
                                                                                                                                                                              
                                                                   
    elif opc0 == '2' :
        break
   
                
 
