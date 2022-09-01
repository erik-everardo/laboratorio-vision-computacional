import sys, os # Importe pygame para la creacion de la ventana
from PIL import Image #Importar para trabajar con modulo Image de (PIL)
from sys import argv # Importe para trabajar con argumentos
import math
import random
 
#Convierte la imagen en escala de grises
def escala_g(image):
    ancho, alto = image.size
    for i in range(ancho):
        for j in range(alto):
            (r,g,b)= image.getpixel((i,j))
            pix = math.trunc((r + g + b)/3)
            image.putpixel((i,j), (pix, pix, pix))

    return image
 
#aplicarumbral
def umb():
    image_filename = argv[1]
    image = Image.open(image_filename)
    image = image.convert("RGB")
    image = escala_g(image)
    ancho, alto = image.size
    minim = random.randint(0,100)
    maxim = random.randint(101,255)
    print("Valor minimo: "+str(minim))
    print("Valor maximo: "+str(maxim))
    for i in range(ancho):
        for j in range(alto):
            # en este punto r, g, y b son iguales
            (r,g,b) = image.getpixel((i,j))
            value = 0
            if (r > maxim):
                value=255
                
            image.putpixel((i,j), (value, value, value))
    nueva = 'luminoso.png'
    image.save(nueva)
  
def main():
    imagen_umbral = umb()
     
if __name__ == "__main__":
    main()
