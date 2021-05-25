##para resolver este problema basicamente se fue hacia una casilla vacia (las que tienen 0 se consideran vacias) e ir probando numeros hasta que se encuentre uno que satisfaga la regla(no puede haber ninguno
##repetido ni en las filas ni en las columnas ni en una misma caja) y luego se pasa a la siguiente casilla y repetir (he ahi la recursividad) y si mas adelante llega a un resultado que no satisfaga la regla
##volvera un paso atras, en caso de que tampoco ningun numero satisfaga la regla, nuevamente volvera atras hasta que alguna conbinacion logre terminar el puzzle.

##Algoritmo PSEUDOCODIGO
##
##Comenzando con un tablero incompleto:
##1 Encuentra un espacio vacío
##2 Intente colocar los dígitos del 1 al 9 en ese espacio
##3 Verifique si ese dígito es válido en el lugar actual según el tablero actual
##4
##  A) Si el dígito es válido, intente llenar el tablero de forma recursiva siguiendo los pasos 1-3.
##  B) Si no es válido, restablezca el cuadrado que acaba de llenar y vuelva al paso anterior.
##5 Una vez que el tablero está lleno según la definición de este algoritmo, hemos encontrado una solución.

import pygame
import time
sudoku = [
    [7,8,0,4,0,0,1,2,0],   ##<----primer vacio que encuentra  el 0 que esta entre el 8 y el 4
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def resolver(x): ##aca se hace uso del backtracking ya que en el 1er for se llama a si misma
##    for i in range(9): ##<-- en caso de querer ver como itera el algoritmo paso a paso se puede descomentar esta parte <--<--<--
##        print (x[i])                                                                                   
##        if i ==8:                                                                                      
##            print("________________________")                                                          
    
    a = busca_vacio(x) ##llama a la funcion que busca casillas vacias
    if not a:      ##si no hay casillas vacias se termina el algoritmo
        return True
    else:
        row, col = a ##si hay alguna se guarda su posicion x,y en varibles

    for i in range(1,10):
        if validar(x, i, (row, col)): ##primero llamamos a la funcion validar para ver si el sudoku no tiene errores logicos
            x[row][col] = i  ## y llenamos una casilla
            if resolver(x): ##luego tratamos de resolver recursivamente nuestro sudoku completo o llegamos a un punto de error donde hay que volver atras
                return True

            x[row][col] = 0 ##llena la casilla con el valor invalido y pasa al siguiente numero eje:si con un 1 es la casilla actual tira un error pone un cero y pasa a probar con un numero 2

    return False
##ejemplo de resolver: primero con la funcion busca_vacio encontramos un 0 en este caso la primera casilla es la que esta en la posicion 0,2 entre el 8 y el 4(8,0,4) y nos da su posicion
##luego se comprueba el sudoku y se agrega el 1 ahi y se comprueba que sea valido, no lo es ya que hay otro 1 en esa misma columna, por lo que se vuelve a llenar con  un 0 y se pasa al 2, tampoco
##se pude porque hay un 2 en la mismca columna y pasa al 3, si se puede, pasa a la siguiente casilla y repite, ahora bien si en un futuro llega a haber un problema con poner ese 3 (que lo habra)
##vuelve 1 casilla atras hasta volver a llegar a la primera y en vez de poner un 3 pone un 4 y repite.

def validar(x, num, pos): ##se crea la funcion que valida si el tablero esta correcto con una bandera en caso contario
    for i in range(9):
        if x[pos[0]][i] == num : ##checkea que un numero cualquiera no se encuentre respetido en las filas 
            return False
    for i in range(9):
        if x[i][pos[1]] == num :##checkea que un numero cualquiera no se encuentre respetido en las columnas
            return False
    ## se revisa la repeticion en las cajas
    boxx = pos[1] // 3   ##esto guarda el valor de la posicion x de la caja (estos son valores de 0,1,2)
    boxy = pos[0] // 3   ##esto guarda el valor de la posicion y de la caja (estos son valores de 0,1,2)
                         ##explicado con la imagen de abajo si box_x=0 y box_y=0 entonces estamos hablando de la caja con los signos "/"
                         ##si fuera 2,2 entonces de la con los signos "#"

    for i in range(boxy*3, boxy*3):     ##se multiplica el valor de la caja por 3 para que asi se logre encontar el numero que esta dentro de la caja
                                              ##ejemplo si quisiera llegar al primer signo de la caja con los "$" cuyo valor en la matriz es de (0,6) que se encuetra en la caja 0,2
                                              ##multiplicamos 0*3 y 2*3
        for j in range(boxx*3, boxx*3):
            if x[i][j] == num : ##revisa si no hay repeticiones de numeros en una misma caja 
                return False

    return True
##    [/,/,/,&,&,&,$,$,$],  para exclarecer los simbolos iguales estan dentro de una misma caja
##    [/,/,/,&,&,&,$,$,$],    0 1 2
##    [/,/,/,&,&,&,$,$,$],  0 x x x
##    [i,i,i,+,+,+,0,0,0],  1 x x x
##    [i,i,i,+,+,+,0,0,0],  2 x x x
##    [i,i,i,+,+,+,0,0,0],
##    [%,%,%,a,a,a,#,#,#],
##    [%,%,%,a,a,a,#,#,#],
##    [%,%,%,a,a,a,#,#,#]

def mostrar(x):
    for i in range(len(x)):
        if i % 3 == 0 and i != 0:   ##cada 3 filas pone un - ya que el modulo de 3 efectivamente es 0 y el 6 
            print("- - - - - - - - - - - - - ")
 
        for j in range(len(x[0])): 
            if j % 3 == 0 and j != 0:##cada 3 columnas agrega un | y seguido de el la siguiente caja sin poner uno al inicio 
                print(" | ", end="")   ## luego pone la siguiente columna 

            if j == 8: ##si llega al ultimo numero de la derecha baja a la siguiente fila sino imprima la siguiente columna al lado de la anterior
                print(x[i][j])
            else:
                print(str(x[i][j]) + " ", end="")##por cuestiones esteticas se agrega un espacio tambien


def busca_vacio(x): ##si encuntra una casilla vacia (con un numero 0) nos regresara su posicion x,y
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] == 0:
                return (i, j)  

    return None

mostrar(sudoku) ##llamamos a la funcion mostrar para ver el sudoku sin hacer
resolver(sudoku)##lamamos a la funcion resolver para resolverlo
print("________________________")
mostrar(sudoku) ##mostramos el sudoku resuelto

