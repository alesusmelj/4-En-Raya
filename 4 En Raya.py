"""Trabajo practico obligatorio 1

    Juego: 4 en raya.

    Integrantes: 
        Bautista Julian
        Alajarin Kevin
        Feresini Franco
        Susmelj Alejandro  
        Witenas Juan Ignacio"""

import random

def crearmatriz ():
    """Crea la matriz que sera el tablero de juego"""

    m = [ ["_"]*8 for i in range (8) ]

    return m
    
def interfazdejuego ():
    """Desarrolla la interfaz de juego basica para el usuario"""

    titulo = "4 EN RAYA"
    titulocentrado = f"{titulo:*^195}"
    print(titulocentrado)
    print("Bienvenido al 4 en raya")
    print()

    while True:

        try:
            reglas = int(input("Si desea leer las reglas presione el número 1, de no querer leerlas presione cualquier número: "))
            print()

        except ValueError as mensaje:
            print()
            print("Ha ingresado un caracter invalido. Ingrese un número.")
            print()

        else:
            break

    if reglas == 1:
        print("""Reglas: 
        El cuatro en raya es un juego  pueden participar 2 personas, en el cual, los oponentes se turnan para dejar caer fichas desde la parte superior. 
        Las fichas ocuparan el siguiente espacio disponible dentro de la columna.

        Cada jugador ganara puntos durante el juego, estos puntos seran guardados en una ranking para poder competir con tus amigos!
        Al principio de la partida, cada jugador empezara con un total de 50 puntos, y se le restara 1 punto por cada turno que el jugador haya jugado.
        Tambien se le agregara 15 puntos al jugador que haya ganado la partida y se le restaran 15 al jugador que haya perdido.      

        La partida termina si una de las siguientes condiciones se cumple: 
        -Uno de los jugadores coloca cuatro o más fichas en una línea contínua vertical, horizontal o diagonalmente. Este jugador gana la partida.
        -Todas las casillas del tablero están ocupadas y ningún jugador cumple la condición anterior para ganar. En este caso la partida finaliza en empate.""")       
        print()

    
    print('Cuando lea "Jugador 1:" o "Jugador 2:" ingrese la letra de la columna en la que desea colocar su ficha.')

    return 

def eleccion (j, eleccion_pasada = 0):

    fichas = ["Fichas:\n", "1:","•\n","2:","X\n","3:","@\n","4:","☻\n","5:","♥\n","6:","♦\n","7:","♠\n","8:","○\n" ,"9:","♂\n","10:","♀\n","11:","♪\n","12:","☼\n"]
    rodaerc = "¢"
    print(*fichas)
    print(j)

    while True:

        try:
            eleccion = input("Ingrese el numero que corresponde a la ficha que desea elegir: ")
            if eleccion == "creador":
                eleccion = easter_egg("creador")
                eleccion = rodaerc
                print("Has descubierto la ficha secreta!")
                return eleccion

            eleccion=int(eleccion)    
            assert eleccion >=1 and eleccion <=12, "Número debe ser entre 1 y 12"
            eleccion = fichas[(eleccion)*2]
            eleccion = eleccion.rstrip("\n")
        
            if eleccion == eleccion_pasada:
                print("Esta ficha ya fue elegida")

            else:
                break

        except AssertionError as mensaje:
            print()
            print("Elija un número entre 1 y 12")
            print()

        except ValueError as mensaje:
            print()
            print("Ha ingresado un caracter invalido. Ingrese un número entre 1 y 12.")
            print()
            
    return eleccion

def imprimirmatriz(m):
    """Imprime la matriz que este en juego"""
    
    print()

    print("A", "B", "C", "D", "E", "F", "G", "H", sep="  ")
    for columnas in range (len(m)):
        for filas in range (len(m)):
            print(matrizvacia[columnas][filas], end="  ")
        print()

    return m

def llenarmatriz(m, pos1, pos2, simbolo):
    """Llena la matriz en la posición indicada por el jugador con el simbolo elegido"""

    largo = len(m) - 1

    if pos1 != -1:

        valor = pos1
        for j in range (len(m)):
            if m[len(m)-1-j][valor] == "_":
                m[len(m)-1-j][valor] = simbolo
                break

    else:

        valor = pos2

        for j in range (len(m)):

            if m[largo-j][valor] == "_" :

                m[largo-j][valor] = simbolo
                break
    
    return m, valor

def empatar(m):
    """Verifica si el juego termino en un empate"""
    
    for i in range(len(m)):

        if m[0][i] == "_":
            
            return False

    return True

def limite_tablero(alto,l,pos):
    """Identifica el limite de cada columna para evitar que se rellene de mas"""

    permitido=True

    if l[pos]+1 <= alto:
        l[pos]+=1

    else:
        permitido = False
    
    return permitido, l

def checker(m, pos, ficha, lista):
    """Analiza horizontal, vertical y diagonalmente si el jugador ganó"""

    cont_h = 0
    cont_v = 0
    cont_d = 0
        
    #Horizontal
    for j in range(len(m)):
       
        if m[len(m)-lista[pos]][j] == ficha:
            cont_h+=1
            
        else:
            cont_h=0

        if cont_h==4:
            return True
            
    #Vertical
    for i in range(len(m)):

        if m[i][pos] == ficha:
            cont_v+=1

        else:
            cont_v=0

        if cont_v==4:
            return True

    #Diagonal positiva
    for c in range(len(m)-4):  
        
        k = (len(m)-1)
        
        if m[k][c] == ficha and m[k-1][c+1] == ficha and m[k-2][c+2] == ficha and m[k-3][c+3] == ficha:
            return True

    #Diagonal negativa
    for a in range(len(m)-4):  
        
        if m[a][a] == ficha and m[a+1][a+1] == ficha and m[a+2][a+2] == ficha and m[a+3][a+3] == ficha: 
            return True

    return False
            
def puntajes (tur1, tur2, win):

    puntosj1 = 50
    puntosj2 = 50

    puntosj1 = puntosj1 - tur1
    puntosj2 = puntosj2- tur2

    if win == 1:

        puntosj1 = puntosj1 + 15
        puntosj2 = puntosj2 - 15

    elif win == 2:

        puntosj2 = puntosj2 + 15
        puntosj1 = puntosj1 - 15

    return puntosj1, puntosj2

def easter_egg(string):
    
        if len(string) == 0:
          return string

        else:
           return easter_egg(string[1:]) + string[0]
           
            
#Programa principal

jugadas_filas = []
estado_de_juego = False
win = False
turnos1 = 0
turnos2 = 0
ganador = 0

try:
    puntaje = open ("Puntaje", "wt")

    dic={
            "A" : 0,
            "B" : 1,
            "C" : 2,
            "D" : 3,
            "E" : 4,
            "F" : 5,
            "G" : 6,
            "H" : 7,
        }

    matrizvacia = crearmatriz()
  
    interfazdejuego()

    print()
    nombre_jugador1 = input("Ingrese su nombre jugador 1: ")
    f1 = eleccion(nombre_jugador1)
    
    print()
    nombre_jugador2 = input("Ingrese su nombre jugador 2: ")
    f2 = eleccion(nombre_jugador2, f1)

    #Esto crea la lista de las columnas usadas
    for i in range(len(matrizvacia)):
        jugadas_filas.append(0)

    imprimirmatriz(matrizvacia)    

    while estado_de_juego == False or win == False:
              
        jugador1 = str(input(F'{nombre_jugador1}: ')).upper()
        jugador1 = dic.get(jugador1, "No existe esa letra.")

        while jugador1 == "No existe esa letra.":

            print(jugador1)
            jugador1 = str(input(F'{nombre_jugador1}: ')).upper()
            jugador1 = dic.get(jugador1, "No existe esa letra.")
            
        limite, jugadas_filas = limite_tablero(len(matrizvacia), jugadas_filas, jugador1)

        while limite != True:

            print()
            print("Ha elegido una columna que esta llena. Elija otra posición")
            print()
            jugador1 = str(input(F'{nombre_jugador1}: ')).upper()
            jugador1 = dic.get(jugador1, "No existe esa letra.")

            while jugador1 == "No existe esa letra.":

                print(jugador1)
                jugador1 = str(input(F'{nombre_jugador1}: ')).upper()
                jugador1 = dic.get(jugador1, "No existe esa letra.")

            limite, jugadas_filas = limite_tablero(len(matrizvacia), jugadas_filas, jugador1)

        turnos1+=1
 
        matriz, jugador1 = llenarmatriz(matrizvacia, jugador1, -1,f1)
        imprimirmatriz(matriz)

        win = checker(matriz, jugador1, f1,jugadas_filas)

        if win == True:

            print()    
            print("¡Has ganado,", nombre_jugador1,"!")
            ganador = 1
            break

        #/////JUGADOR 2//////
           
        jugador2 = str(input(F'{nombre_jugador2}: ')).upper()
        jugador2 = dic.get(jugador2, "No existe esa letra.")

        while jugador2 == "No existe esa letra.":

            print(jugador2)
            jugador2 = str(input(F'{nombre_jugador2}: ')).upper()
            jugador2 = dic.get(jugador2, "No existe esa letra.")
    
        limite, jugadas_filas = limite_tablero(len(matrizvacia), jugadas_filas, jugador2)
            
        while limite != True:

            print()
            print("Ha elegido una columna que esta llena. Elija otra posición")
            print()
            jugador2 = str(input(F'{nombre_jugador2}: ')).upper()
            jugador2 = dic.get(jugador2, "No existe esa letra.")

            while jugador2 == "No existe esa letra.":

                print(jugador2)
                jugador2 = str(input(F'{nombre_jugador2}: ')).upper()
                jugador2 = dic.get(jugador2, "No existe esa letra.")
                    
            limite, jugadas_filas = limite_tablero(len(matrizvacia), jugadas_filas, jugador2)

        turnos2+=1

        matriz, jugador2 = llenarmatriz(matrizvacia, -1, jugador2, f2)

        imprimirmatriz (matriz)
    
        win = checker(matriz, jugador2, f2, jugadas_filas)

        if win == True:

            print()
            print("¡Has ganado,", nombre_jugador2, "!")
            ganador = 2
            break

        estado_de_juego = empatar(matriz)
            
        if estado_de_juego:
            print()
            print("La partida ha terminado en empate.")
            break

        print()

    pun1, pun2 = puntajes(turnos1, turnos2, ganador)

    pun1 = str(pun1)
    pun2 = str(pun2)

    if ganador == 1:

        escrito = ["Puntajes:\n", "\n*Puntos iniciales: 50.\n", "*Se resta 1 punto por cada turno que el jugador haya jugado.\n", 
                    "*Se le agregan 15 puntos al jugador que haya ganado y se le restan 15 puntos a quien haya perdido.\n\n", nombre_jugador1, ": ", pun1, " --> GANADOR","\n", nombre_jugador2,": ", pun2, " --> PERDEDOR"]

    elif ganador == 2:

        escrito = ["Puntajes:\n", "\n*Puntos iniciales: 50.\n", "*Se resta 1 punto por cada turno que el jugador haya jugado.\n", 
                    "*Se le agregan 15 puntos al jugador que haya ganado y se le restan 15 puntos a quien haya perdido.\n\n", nombre_jugador1, ": ", pun1, " --> PERDEDOR","\n", nombre_jugador2,": ", pun2, " --> GANADOR"]

    else:

        escrito = ["Puntajes:\n", "\n*Puntos iniciales: 50.\n", "*Se resta 1 punto por cada turno que el jugador haya jugado.\n", 
                   "*Se le agregan 15 puntos al jugador que haya ganado y se le restan 15 puntos a quien haya perdido.\n", "\nLa partida ha terminado en empate\n", nombre_jugador1, ": ", pun1,"\n", nombre_jugador2,": ", pun2,]

    puntaje.writelines(escrito)

finally:
        
    try:
        puntaje.close()

    except NameError:
        pass
