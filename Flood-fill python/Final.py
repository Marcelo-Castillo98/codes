import cv2
import numpy as np
import matplotlib.pyplot as plt ##libreia encargada de plotear la imagenes
puntero=(177,35)                ##aqui va el puntero que es el que decide donde se pinta
img=cv2.imread('colores.png')  ## se carga la imagen
f= img.copy()                  ##se copia la imagen y se guarda en una variable
cv2.floodFill(f,None,puntero,(200,0,0),(2,2,2,2),(1.2,2,2,2)) ## se le pasa la imagen, la pocicion inicial y el color (200,0,0)=AZUL en bgr), los ultimos 2 datos son la tolerancia al color que
                                                                    ##usa para que el rellenado se vea mejor ya que tolera mayor cantidad de tonos, en el pdf se muestra la diferencia visual
cv2.circle(f,puntero,4,(0,0,255),2)   ##se dibuja un circulo para que se note donde partio el punto inicial
imgs=[img,f]  ##se  generan arrleglos que contiene las imagenes
t=['original','rellenado']  ##se agregan los titulos

for i in range(2):  ##se  grafican las imagenes
    plt.subplot(1,2,i+1) ## se crea un subplot de 1 fila x 2 columnas
    plt.imshow(cv2.cvtColor(imgs[i], cv2.COLOR_BGR2RGB),vmin=0,vmax=255)##se  muestran las imagenes en formato rgb con minimos de 0 y maximos de 255
    plt.title(t[i]) ##se muestran los titulos
    plt.xticks([]),plt.yticks([]) ##es para que no se muestre la numeracion de las img
plt.show()    
