import pygame
pygame.font.init()

sudoku = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
##sudoku=[         [1, 0, 5, 4, 6, 2, 9, 8, 7],  ##otro sudoku para probar el algoritmo
##                 [7, 6, 2, 1, 0, 8, 5, 4, 3],
##                 [8, 0, 4, 5, 3, 7, 6, 2, 0],
##                 [9, 7, 8, 6, 1, 3, 2, 0, 4],
##                 [4, 1, 6, 9, 2, 0, 3, 7, 8],
##                 [2, 5, 3, 7, 0, 4, 1, 6, 9],
##                 [5, 0, 7, 3, 4, 1, 0, 9, 6],
##                 [3, 8, 9, 2, 7, 6, 4, 1, 5],
##                 [0, 4, 0, 8, 5, 9, 7, 0, 2]
##    ]
class Grid:


    def __init__(self, rows, cols, width, height):##iniciamos la clase grid con los parametros de las filas,columnas alto y ancho
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(sudoku[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height

        
    def draw(self, win):   ##dibujamos las lineas y los cubos en pygame
        gap = self.width / 9 ##calcula la distancia de los cubos dividiendo el ancho total en 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0: ##cada 3 cajas hace una linea gruesa y si no una linea delgada
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick) ##dibuja las lineas horizontales
            pygame.draw.line(win, (0,0,0), (i*gap, 0), (i*gap,self.height), thick) ##dibuja las lineas verticales
        ##dibuja los cubos
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win) 

class Cube:    ##definimos la clase cubo que contendra y mostrara los numeros corresponsientes
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width ,height): ##definimos la clase cube que contiene los parametros valor=el numero que hay en la matriz,como su posicion (fila,columna) y su alto y ancho.
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height


    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40) ##dibujamos los cubos

        gap = self.width / 9 ##calcula la distancia de los cubos dividiendo el ancho total en 9
        x = self.col * gap   ##setea el tamaño de los cubos
        y = self.row * gap   ##setea el tamaño de los cubos
        if not(self.value == 0):                             
            text = fnt.render(str(self.value), 1, (0, 0, 0))        ##dibuja los numeros
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))
            
def resolver(x): ##aca se hace uso del backtracking ya que en el 1er for se llama a si misma
    for i in range(9): ##<-- en caso de querer ver como itera el algoritmo paso a paso se puede descomentar esta parte <--<--<--
        print (x[i])                                                                                   
        if i ==8:                                                                                      
            print("________________________")                                                          
    
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

    for i in range(boxy*3, boxy*3+3):     ##se multiplica el valor de la caja por 3 para que asi se logre encontar el numero que esta dentro de la caja
                                              ##ejemplo si quisiera llegar al primer signo de la caja con los "$" cuyo valor en la matriz es de (0,6) que se encuetra en la caja 0,2
                                              ##multiplicamos 0*3 y 2*3
        for j in range(boxx*3, boxx*3+3):
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
def redraw_window(win, x):
    win.fill((255,255,255))
    x.draw(win)
def main():
    win = pygame.display.set_mode((540,600))
    pygame.display.set_caption("Sudoku")
    key = None
    run = True
    ##mostramos la pantalla con el sudoku sin hacer
    redraw_window(win, Grid(9, 9, 540, 540))
    pygame.display.update()
    ##mostramos por consola el sudoku sin hacer
    mostrar(sudoku)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: ##se resulve el sudoku si precionamos la tecla "ENTER"
                    ##resolvemos el sudoku
                    resolver(sudoku)##lamamos a la funcion resolver para resolverlo
                    print("________________________")
                    mostrar(sudoku) ##mostramos el sudoku resuelto
                    ##actualizamos la pantalla
                    redraw_window(win, Grid(9, 9, 540, 540))
                    pygame.display.update()

main() ##llamamos al metodo main
pygame.quit()

