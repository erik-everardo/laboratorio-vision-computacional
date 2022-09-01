from PIL import Image
from math import*
import math
from PIL import Image
from sys import argv # Importe para tabajar con argumentos


def main():
    contraste()
    

def contraste():
    #toma imagen en escala de grises
	image = Image.open(argv[1])
	ancho,alto = image.size
	minimo = int(argv[2]) #toma un valor umbral minimo
	for i in range(ancho):
		for j in range(alto):
			(r,g,b) = image.getpixel((i,j))
			escala = math.trunc((r + g + b)/3)		
			image.putpixel((i,j), (escala,escala, escala))
			if r < minimo:
				p=0
			else:
				p= 255
				
			image.putpixel((i,j), (p,p,p))

	new = 'contraste.png'
	image.save(new)

if __name__ == "__main__":
    main()
