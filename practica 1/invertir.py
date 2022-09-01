import sys
from PIL import Image 
from sys import argv 
import numpy

def main():
    image,ancho,alto= invertir(argv[1])
    
def invertir(image):
    image = Image.open(image)
    image = image.convert("RGB")
    new_image = 'invertir.png'
    pixels = image.load()
    umbral = 0.8
    ancho,alto = image.size
    #matriz = numpy.empty((ancho, alto))
    for i in range(ancho):
        for j in range(alto):
            (r,g,b) = image.getpixel((i,j))
            rr = (255-r)
            rg = (255-g)
            rb = (255-b)
            #escala = (rr+rg+rb)
            pixels[i,j] = (rr,rg,rb)
            #matriz[i,j] = int(escala)
    image_filtro = image.copy()

    image = image.save(new_image)
    return image_filtro,ancho,alto
           
main()
