import sys
from PIL import Image 
from sys import argv 
import numpy

def main():
    image= tono(argv[1])
 
def tono(image):
    imagen = Image.open(image)
    imagen = imagen.convert("RGB")
    new_image = 'tono.png'
    #umbral = 0.8
    print("Especifica el tono (r, g o b)")
    opcion = input()
    ancho,alto = imagen.size
    #matriz = numpy.empty((ancho, alto))
    for i in range(ancho):
        for j in range(alto):
            (r,g,b) = imagen.getpixel((i,j))
        
            #selecciona r, g o b para cambiar el tono
            if(opcion == "r"):
                imagen.putpixel((i,j),(r,0,0))
            if(opcion == "g"):
                imagen.putpixel((i,j),(0,g,0))
            if(opcion == "b"):
                imagen.putpixel((i,j),(0,0,b))

    imagen.save(new_image)
    imagen.show()
    return ancho,alto
           
main()

