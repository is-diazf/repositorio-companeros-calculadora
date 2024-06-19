#este es el archivo py en el q trabajaremos con mis ñeros pa crear una calculadora entre todos
#pq si la pone uno, la ponen todos
#THE GAME

#pegate un saque compañero
#creo que así se soluciona
#gei el que lee
#wekito
numero1= 0
numero2= 0
def sumar(numero1, numero2):
    resultadoS = numero1 + numero2;
    return resultadoS;

def restar(numero1, numero2):
    resultador= numero1 - numero2;
    return resultador;

def multiplicar(numero1, numero2):
    resultadoM = numero1 * numero2;
    return resultadoM;

def dividir(numero1, numero2):
    try:
        resultadoD= numero1 / numero2;
    except ZeroDivisionError:
        resultadoD = "no se puede dividir por cero"
    finally:
        return resultadoD;

while True:
    op= int(input("1.- Suma.\n2.- Resta.\n3.- Multiplicación.\n4.- División.\n5.- Salir."))
    match op:
        case 1:
            sumar(numero1,numero2)
        case 2:
            restar(numero1,numero2)
        case 3:
            multiplicar(numero1,numero2)
        case 4:
            dividir(numero1,numero2)
        case 5:
            break
        case _:
            print("ingrese una opción válida, no sea weon.")

    print