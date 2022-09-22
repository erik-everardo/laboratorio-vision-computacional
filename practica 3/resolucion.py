from ast import arg
from PIL import Image
from math import floor
import numpy as np
from sys import argv

def main():

    im = Image.open(argv[1])
    (ancho,alto) = im.size
    imagen = im.load()
    im.show()
    
    print("Tamano original: ", ancho,alto)
    x = int(argv[2])
    y = int(argv[3])
    mide_ancho = (1.0*x)/ancho
    mide_alto = (1.0*y)/alto
    n_ancho = int(ancho*mide_ancho)
    n_alto = int(alto*mide_alto)
    
    nueva = Image.new('RGB',(n_ancho,n_alto))

    print("Nuevo tamano: ", n_ancho,n_alto)
    otra = nueva.load()
    
    res = aum_dis(nueva,imagen,otra,mide_ancho,mide_alto,n_ancho,n_alto)
    res.save("resolucion.png")


def aum_dis(im,imagen,otra,mide_ancho,mide_alto,n_ancho,n_alto):
    
    for a in range(n_ancho):
        for b in range(n_alto):
            otra[a,b] = imagen[int(a/mide_ancho),int(b/mide_alto)]

    return im
    
if __name__ == '__main__':
    main()

