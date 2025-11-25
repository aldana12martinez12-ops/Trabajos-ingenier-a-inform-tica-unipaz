def mostrar_menu():
    print("menu principal")
    print("1. registrarse")
    print("2. iniciar sesión")
    print("3. salir")

while 'true':
    mostrar_menu()  
    opc = input("seleccione una opcion: ") 
     
    if opc == '1' :
        cuentas = {
    "andres":"123"
    } 
        reg_cuenta = input("registre su cuenta: ")     
        reg_contraseña = input("registre su             contraseña: ")
        cuentas[reg_cuenta] = reg_contraseña
        print("registro exitoso")
        
    elif opc == '2' :
        cuenta = input("ingrese su cuenta: ")
        contraseña = input ("ingrese su contraseña: ")
        k = 0
        if cuenta in cuentas and contraseña                     == cuentas[cuenta]:
                        print("inicio de sesion exitoso")
                        k = 1
        if k == 0:
            print("error")    
    elif opc == '3':
        break               