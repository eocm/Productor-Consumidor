import time
import random
import msvcrt
import os

contenedor = []

def main():
    indice_consumidor = 0
    indice_productor = 0
    total_a_producir = 0
    total_a_consumir = 0
    contador = 0
    
    for i in range(25):
        contenedor.append("_") #Lleno el contenedor de guiones

    while True:
        turno = random.randint(0, 1) # 0 = productor, 1 = consumidor
        productor = random.randint(2, 5) # Productor produce entre 2 y 5 elementos
        consumidor = random.randint(2, 5) # Consumidor consume entre 2 y 5 elementos
        if(msvcrt.kbhit()):
            key = msvcrt.getwch()
            #Tecla ESC
            if(key == chr(27)):
                break

        if(turno == 0): # Productor
            contador = 0
            for i in range(productor):
                if indice_productor + 1 > 24: # Si el indice del productor es mayor a 24, el siguiente indice es 0
                    siguiente = 0 # Siguiente indice
                else:
                    siguiente = indice_productor + 1 # Siguiente indice
                if len(contenedor) == 25 and contenedor_lleno() != True: # Si el contenedor tiene 25 elementos y no está lleno
                    print ("\nNúmero al azar: ", turno)
                    print ("0 = Productor")
                    print ("1 = Consumidor\n")
                    print ("\n---- Turno del PRODUCTOR ----\n")    
                    contenedor[indice_productor] = "@"
                    contador += 1
                    indice_productor += 1
                    total_a_producir = productor # Total de elementos a producir por iteracion
                    if(indice_productor == 25):
                        indice_productor = 0
                    total_a_consumir = 0
                    imprimir(total_a_producir, total_a_consumir, contador)
                    #imprimo el indice del contenedor debajo de este del 1 al 25
                    for i in range(25):
                        #salto de linea
                        if(i == 0):
                            print("\n")
                        if (i < 9):
                            print(i+1, end="  ")
                        else:
                            print(i+1, end=" ")
                        

                    time.sleep(1)
                    clearConsole()
            

        elif(turno == 1): # Consumidor
            contador = 0
            for i in range(consumidor):
                
                if indice_consumidor + 1 > 24: # Si el indice del consumidor es mayor a 24, el siguiente indice es 0
                    siguiente = 0
                else:
                    siguiente = indice_consumidor + 1
                if len(contenedor) == 25 and contenedor_vacio() != True and (contenedor[siguiente] == "@" or contenedor[indice_consumidor] == "@"): # Si el contenedor tiene 25 elementos y no está vacío y el siguiente elemento o el elemento actual es @
                    print ("\nNúmero al azar: ", turno)
                    print ("0 = Productor")
                    print ("1 = Consumidor\n")
                    print ("\n---- Turno del CONSUMIDOR ----\n")
                    contenedor[indice_consumidor] = "_"
                    contador += 1
                    indice_consumidor += 1
                    total_a_consumir = consumidor
                    if(indice_consumidor == 25):
                        indice_consumidor = 0
                    total_a_producir = 0
                    imprimir(total_a_producir, total_a_consumir, contador)
                    #imprimo el indice del contenedor debajo de este del 1 al 25
                    for i in range(25):
                        #salto de linea
                        if(i == 0):
                            print("\n")
                        if (i < 9):
                            print(i+1, end="  ")
                        else:
                            print(i+1, end=" ")
                    time.sleep(1)
                    clearConsole()

def imprimir(tp, tc, c):
    #Si el productor esta dormido, impirme en pantalla que esta dormido
    if(tp == 0):
        print ("Productor producirá: Dormido")
    else:
        print ("Productor producirá: ", tp)
    if (tc == 0):
        print ("Consumidor consumirá: Dormido")
    else:   
        print ("Consumidor consumirá: ", tc)
        
    if tc > 0:
        print ("\nConsumiendo...\n")
        print ("\nNúmero de elementos consumidos: ", c ,"\n")
    elif tp > 0:
        print ("\nProduciendo...\n")
        print ("\nNúmero de elementos producidos: ", c, "\n")
    #print ("Contenedor: ", contenedor)
    # Imprimo el contenido del contenedor
    for i in range(25):
        print (contenedor[i], end="  ")
    
    """for i in range(25): # Imprimo el contenedor
        print(contenedor[i], end=" ")"""

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def contenedor_vacio():
    cont = 0

    for i in range(25):
        if(contenedor[i] == "_"):
            cont += 1
    if(cont == 25):
        return True
    return False

def contenedor_lleno():
    cont = 0
    
    for i in range(25):
        if(contenedor[i] == "@"):
            cont += 1
    if(cont == 25):
        return True
    return False

main()