#3.1
x = 2
y = 3
if (x > y):
    result = x
else:
    result = y
#ten kod jest poprawny

#for i in "qwerty": if ord(i) < 100: print i
#ten kod nie jest poprawny
#nalezy go napisac tak:
for i in "qwerty":
	if ord(i) < 100:
		print i

for i in "axby": print ord(i) if ord(i) < 100 else i
#tak jest poprawny


#3.2
L = [3, 5, 4]
L = L.sort()
#składniowo jest dobrze, ale nie ma sensu

x, y, z = 1, 2, 3

# X = 1, 2, 3 cyfry nalezy zapisac w nawiasach kwadratowych
X = [1, 2, 3]
X[1] = 4

X = [1, 2, 3] 
# X[3] = 4 zle bo liczymy od 0

X = "abc" 
X+="d" #napis nie ma metody append

map(lambda x: pow(x,2), range(8)) 

