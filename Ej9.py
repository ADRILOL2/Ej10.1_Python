def potencia(n):
	a=[]
	for e in range(10):
    		a.append(e**n)
	return a

print(potencia(3))

def prova(n):
	return [x**n for x in range(10)]

n=int(input("escribe un numero,la cantidad que pongas sera el numero que elevara una lista del 0 al 9:"))
for i in range(n):
    print(prova(i)) # Aquí li passem el número al qual volem elevar els elements de la llista
