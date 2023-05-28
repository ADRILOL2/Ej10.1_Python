def lparaulaf(l):
	ll=[]
	a = l.split(" ")
	for e in a:
		ll.append(len(e))
	return ll

print(lparaulaf("hola, avui fa bon temps i ho aprofitarem"))

def lenp(frase):
	return list(map(len,frase.split(" ")))#significa que se separa entre los espacios de la frase

print(lenp("Hola, això és una prova d’una frase qualsevol"))
