#4,2

#3.5
n = int(input("Podaj dlugosc miarki: "))
def miarka(n):
    output = '|'
    for x in range(n):
	    output += '....|'
	    x = x +1
    output += '\n0'
    for x in range(n):
	    next_x = x + 1
	    x = str(next_x)
	    next_x = len(x)
	    while (5 - next_x):
		    output += ' '
		    next_x += 1
	    output += x
    return output

out = miarka(n)
print(out)


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

out = rysuj_kratke(x, y)
print(out)
