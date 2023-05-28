class animal:
    def __init__(self,especie,edad):
        self.especie=especie
        self.edad=edad
    def charla(self):
        pass
    def moverse(self):
        pass
    def quiensoy(self):
        print("soy un...{}".format(self.especie))

class caballo(animal):
    def charla(self):
        print("hiiiii")
    def moverse(self):
        print("Me muevo trotando")

class delfin(animal):
    def charla(self):
        print("Txas")
    def moverse(self):
        print("Me muevo por el agua.")

class abeja(animal):
    def charla(self):
        print("Bzzzzzz")
    def moverse(self):
        print("Me muevo volando")
    def picar(self):
        print("me jodes, te pico")

class humano(animal):
    def __init__(self, especie, edad,nombre):
        super().__init__(especie, edad)
        self.nombre=nombre
    def charla(self):
        print("Hola")
    def moverse(self):
        print("Me muevo caminando")
    def quiensoy(self):
        print("Me llamo {}".format(self.nombre))

class hijo(humano):
    def __init__(self, especie, edad,nombre,padres):
        super().__init__(especie, edad, nombre)
        self.padres=padres
    def nombrepadres(self):
        print("Mi padre se llama {} y mi madre {}".format(self.padres[0],self.padres[1]))

class centauro(caballo,humano):
    def quiensoy(self):
        print("soy un centauro y surjo de {}".format(centauro.__mro__))

class xou:
    def quiensoy(self):
        print("duck type, asi soy yo")
    def moverse(self):
        print("duck type, asi me muevo")
    def charla(self):
        print("duck type, asi hablo")

f=[humano("humano",32,"joan"),caballo("mamifero",10),delfin("mamifero",23),abeja("insecto",1),hijo("humano",6,"Pau"("Joan","Luz")),xou(),centauro("centauro",40,"Quiron")]
for e in f:
    e.quiensoy()
    e.moverse()
    e.charla()
    if type(e)==hijo:
        e.nompares()
    elif type(e)==abeja:
    	e.picar()