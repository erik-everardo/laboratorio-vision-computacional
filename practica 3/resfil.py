#!/usr/bin/python
#from Tkinter import *
from logging import exception
from PIL import Image
from math import floor
from sys import argv
import numpy as np



#def normalizar(imagen_original):


#    x, y = imagen_original.size
#    imagen_normalizada = Image.new("RGB", (x, y))
#    pixeles = []
#    for a in range(y):
#        for b in range(x):
#            pix = imagen_original.getpixel((b, a))[0]
#            pixeles.append(pix)
#    maximo = max(pixeles) 
#    minimo = min(pixeles)
#    print maximo
#    print minimo
#    l = 256.0/(maximo - minimo)
#    pixeles = []
#    for a in range(y):
#        for b in range(x):
#            pix = imagen_original.getpixel((b, a))[0]
#            nuevo_pix = int(math.floor((pix-minimo)*l))
#            pixeles.append((nuevo_pix, nuevo_pix, nuevo_pix))
#    imagen_normalizada.putdata(pixeles)
#    imagen_normalizada.save("imagen_normalizada.png")
#    return imagen_normalizada

#def filtro(imagen_original):
    #se encarga de tomar de cada pixel los pixeles 
    #de izq, derecha, arriba, abajo y el mismo y los promedia, y ese
    #promedio es el valor de los nuevos pixeles
    
#    x, y = imagen_original.size
#    imagen_difusa = Image.new("RGB", (x, y))
#    pixeles = []
    #temp sirve para obtener el promedio de los
    #pixeles contiguos 
#    temp = []
#    for a in range(y):
#        for b in range(x):
#            actual = imagen_original.getpixel((b, a))[0]
#            if b>0 and b<(x-1) and a>0 and a<(y-1):
                    #en esta condicion entran todos los pixeles que no estan
                    #en el margen de la imagen, es decir casi todos
#                pix_izq = imagen_original.getpixel((b-1, a))[0]
#                pix_der = imagen_original.getpixel((b+1, a))[0]
#                pix_arriba = imagen_original.getpixel((b, a+1))[0]
#                pix_abajo = imagen_original.getpixel((b, a-1))[0]
#                temp.append(pix_izq)
#                temp.append(pix_der)
#                temp.append(pix_arriba)
#                temp.append(pix_abajo)
#            else:
                #aqui entran todos los pixeles de la orilla
#                try:
#                    pix_abajo = imagen_original.getpixel((b, a-1))[0]
#                    temp.append(pix_abajo)
#                except:
#                    pass
#                try:
#                    pix_der = imagen_original.getpixel((b+1, a))[0]
#                    temp.append(pix_der)
#                except:
#                    pass
#                try:                
#                    pix_izq = imagen_original.getpixel((b-1, a))[0]
#                    temp.append(pix_izq)
#                except:
#                    pass
#                try:
#                    pix_arriba = imagen_original.getpixel((b, a+1))[0]
#                    temp.append(pix_arriba)
#                except:
#                    pass
#            temp.append(actual)
                #se obtiene el promedio para cambiar el pixel
#            prom = sum(temp)/len(temp)
#            temp = []
#            pixeles.append((prom, prom, prom))
#    imagen_difusa.putdata(pixeles)
#    imagen_difusa.save("imagen_difusa.png")
#    return imagen_difusa

def hacer_gris(imagen_original):
    """pone la foto en escala de grises
    toma el valor maximo del rgb de cada pixel
    """
    x, y = imagen_original.size
    imagen_gris = Image.new("RGB", (x,y))
    pixeles = []
    for a in range(y):
        for b in range(x):
            r, g, b = imagen_original.getpixel((b, a))
            rgb = (r, g, b)
                #se elige el valor mas grande
            maximo = max(rgb)
            data = (maximo, maximo, maximo)
            pixeles.append(data)
    imagen_gris.putdata(pixeles)
    imagen_gris.save("imagen_gris.png")
    return imagen_gris

#def resolucion(imagen_original):
    #x, y = imagen_original.size
    #imagen_gris = Image.new("RGB", (x,y))
def resolucion_imagen(pix_antes, ancho_original, altura_original, ancho, alto):
   
    mancho = (ancho_original * 1.0) / ancho
    malto = (altura_original * 1.0) / alto

    imagen_n = np.zeros( (alto, ancho, 3) )

    for a in range(ancho):
        for b in range(alto):
            Pos_x = floor( a * mancho)
            Pos_y = floor( b * malto)
            
            try:
               
                imagen_n[a,b] = pix_antes[int(Pos_x), int(Pos_y)]
            except IndexError:
                print('\nPosicionX:', a, 'PosicionY:', b)
                print( 'Posx:', Pos_x, 'Posy', Pos_x)
                print(imagen_n.size)
                print(imagen_n.shape)
                return pix_antes
                
    return imagen_n

def main():
    """funcion principal
    """
    try:
        imagen_inicial = argv[1]
        print(imagen_inicial)
        imagen_original = Image.open(imagen_inicial).convert('RGB')
        #imagen_original = imagen_o.convert('RGB')
        #imagen_original.show()
        (x,y) = imagen_original.size
        print('Medidas de imagen_original:', x,y)
        imagen_original_array = np.array(imagen_original)
        toma_ancho = int(argv[2])
        toma_alto = int(argv[3])
        
        imagen_n = resolucion_imagen(imagen_original_array, x, y, toma_ancho,toma_alto)

        Image.fromarray(np.uint8(imagen_n)).save("resfil.png")

    except ValueError:
        print("nueva dimension:", toma_ancho, toma_alto)
    
        
if __name__ == "__main__":
    main()
