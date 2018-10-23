#3.10
print('Zad 3.10')
slownik = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def roman2int(liczba):
	lista = list(liczba)
	poprzednia = lista[0]
	number = 0
	for index in range(1, len(lista)):
		if(slownik[lista[index]] <= slownik[poprzednia]):
			number += slownik[poprzednia] 
		else:
			number -= slownik[poprzednia]
		poprzednia = lista[index]
	number += slownik[lista[len(lista)-1]]
	return number
	
	
L = ["MCLXIV", "IV", "VII", "XIX", "XL", "XCV", "CM", "MXXV", "MCMXCV", "MM", "MCMLVI", "MMXI", "MMMDCCCLXXXVIII"]

print(L)
for x in L:
	print(roman2int(x))
	
