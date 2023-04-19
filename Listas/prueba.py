from tienda import Tienda

#Objeto de la clase Tienda
tiendita = Tienda()

#Menú
while True:
    print("1. Dar de alta un producto")
    print("2. Dar de baja un producto")
    print("3. Consultar un producto")
    print("4. Modificar un producto")
    print("5. Salir")
    op = int(input("Ingrese una opción: "))
    print()
    
    match op:
        case 1:
            clave = input("Ingrese la clave del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            inf = input("Ingrese la descripción del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese las existencias del producto: "))
            print()
            print(tiendita.alta(clave,nombre,inf,precio,cantidad))
        case 2:
            clave = input("Ingrese la clave del producto: ")
            print()
            if tiendita.validar(clave):
                print(tiendita.baja(clave))
        case 3:
            print("1. Consultar por clave")
            print("2. Consultar por nombre")
            print("3. Consultar todos los productos")
            consulta = int(input("Ingresa una opción: "))
            print()
            match consulta:
                case 1:
                    clave = input("Ingrese la clave del producto: ")
                    print()
                    print(tiendita.consultarC(clave))
                        
                case 2:
                    nombre = input("Ingrese el nombre del producto: ")
                    print(tiendita.consultarN(nombre))
                case 3:
                    print(tiendita.consultar())
        case 4:
            pass
        case 5:
            break
        
