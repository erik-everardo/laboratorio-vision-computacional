from PIL import Image
from math import*
import math
from PIL import Image
from sys import argv # Importe para tabajar con argumentos


def main():
    contraste()
    

def contraste():
    #toma imagen en escala de grises
	image1 = Image.open(argv[1])
	pixels = image1.load()
	ancho,alto = image1.size
	minimo = int(argv[2]) #toma un valor umbral minimo
	for i in range(ancho):
		for j in range(alto):
			a = pixels[i,j]
			escala = math.trunc((a[0] + a[1] + a[2])/3)		
			pixels[i,j] = (escala,escala, escala)
			if pixels[i,j][1] < minimo:
				p=0
			else:
				p= 255
				pixels[i,j]=(p,p,p)

	new = 'contraste.png'
	image1.save(new)

if __name__ == "__main__":
    main()
