from PIL import Image
from sys import argv,exit
from math import floor
import numpy as np

# Parametros: Nuevas dimensiones
x = int(argv[2])
y = int(argv[3])

"""def procesar(im,w,h,pixeles,pix,scale_i,scale_j):
    salto = 0
    for i in range(w):
        for j in range(h):
            for x in range(scale_i):
                for y in range(scale_j):
                    salto = i*scale_i
                    salto2 = j*scale_j
                    pix[salto+x,salto2+y] = pixeles[i,j]
    return im
"""

def escalar(pixeles,scale_i,scale_j,nw,nh):
    pix = np.zeros((nh,nw,3))
    for i in range(nw):
        for j in range(nh):
            pix[i,j] = pixeles[int(i/scale_i),int(j/scale_j)]

    return Image.fromarray(np.uint8(pix))

def main():
    im = Image.open(argv[1]).convert("RGB")
    w,h = im.size
    pixeles = np.array(im)
    im.show()

    scale_i = (1.0*x)/w
    scale_j = (1.0*y)/h

    nw = int(w*scale_i)
    nh = int(h*scale_j)

    
    resized = escalar(pixeles,scale_i,scale_j,nw,nh)
    resized.save("ad.png")

if __name__ == '__main__':
    main()

