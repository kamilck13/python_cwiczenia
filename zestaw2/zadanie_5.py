#3.5
n = int(input("Podaj dlugosc miarki: "))
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
print(output)
