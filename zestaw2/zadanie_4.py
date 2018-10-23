#3.4
while True:
	try:
		line = (input("Podaj liczbe: "))
		n = int(line)
		print(str(n) + ' ' + str(pow(n, 3)))
		
	except ValueError:
		if(line == 'stop'):
			break;
		print('Nie podales liczby! Sprobuj jeszcze raz')
