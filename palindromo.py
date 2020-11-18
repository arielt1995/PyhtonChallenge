import math as ma 
def calcularCaracteresFaltantes(palabra):
	palabra = list(palabra)
	n = len(palabra) 
	countCharacter = 0

	for i in range(n//2): 
		if(palabra[i]== palabra[n-i-1]): 
			continue
		countCharacter+= 1
		
		if(palabra[i]<palabra[n-i-1]): 
			palabra[n-i-1]= palabra[i] 
		else: 
			palabra[i]= palabra[n-i-1] 

	print("Minimo de caracteres a reemplazar para que sea palindromo = ", str(countCharacter)) 