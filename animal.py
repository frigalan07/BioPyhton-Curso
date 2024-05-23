
class animal():
    
    def __init__(self,nombre, edad):
        #Atributos de instancia
        self.nombre = nombre
        self.edad = edad

    #Método haz ruido
    def haz_ruido(self):
        print("AAAAAAAAAAAAH")


class perro(animal):
    #Overriding
    def haz_ruido(self):
        print("¡Guau!")


class gato(animal): 
    def __init__(self, nombre, edad, usa_arenero):
        super().__init__(nombre, edad) #Para inicializar los atrbutos heredados
        self.usa_arenero = usa_arenero
    
    def haz_ruido(self):
        print("¡Miau!")


#Creamos los objetos 
freya = perro("Freya", 7)
senna = gato("Senna", 1, True)

#Hacemos que impriman sus ruidos
freya.haz_ruido()
senna.haz_ruido()

#Imprimimos los diccionarios
print(freya.__dict__)
print(senna.__dict__)

