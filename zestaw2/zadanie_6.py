#3.6
x = int(input("Podaj wartosc x: "))
y = int(input("Podaj wartosc y: "))

def linia_ze_spacjami(dlugosc):
	output = '|'
	for x in range(dlugosc):
		output += '   |'
	return output + '\n'

def linia_z_plusami(dlugosc):
	output = '+'
	for x in range(dlugosc):
		output += '---+'
	return output + '\n'

def rysuj_kratke(dlugosc, wysokosc):
	output = ''
	for x in range(wysokosc):
		output += linia_z_plusami(dlugosc)
		output += linia_ze_spacjami(dlugosc)
	output += linia_z_plusami(dlugosc)
	return output

output = rysuj_kratke(x, y)
print(output)
