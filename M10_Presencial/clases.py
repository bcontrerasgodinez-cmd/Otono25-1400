<<<<<<< HEAD
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Megan")

def area_rectangulo(largo, ancho):
    """Calcula y devuelve el área de un rectángulo."""
    return largo * ancho

# 1. Pedir ancho y largo
largo = int(input("Dime el número del largo: "))
ancho = int(input("Dime el número del ancho: ")) 

# 2. Llamar a la función para obtener el resultado
resultado = area_rectangulo(largo, ancho)

# 3. Mostrar el resultado
print(f"El largo es: {largo}")
print(f"El ancho es: {ancho}")
print(f"El área del rectángulo es: {resultado}")
=======

"""1. Función de saludo"""
def saludo(nombre):
   print(f"Hola, {nombre}!")


saludo("Megan")
saludo("Ana")

"""2. Función para calcular el área de un rectángulo
def area_rectangulo(largo, ancho):
    return largo * ancho
"""

"""3. Class"""
>>>>>>> 9598e239894168af3ecca2350313d2a4a102dfc1

class Gato:
    #funcion requerida
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def maullar(self):
<<<<<<< HEAD
        return "Miau!"    
#Crear objetos    
tu_gato = Gato("Luna", 2) 
otro_gato = Gato("Plutarco", 8)
print(tu_gato.maullar())

class Carro:
    def __init__(self, color, llantas):
        self.color = color
        self.llantas = llantas
mi_auto = Carro("Amarillo", 4)     
print(f"Mi carro es de color {mi_auto.color} y tiene {mi_auto.llantas} llantas.")

# parte 5
#TODO 1 y 3
=======
        return "Miau!"
    
#crear objetos
tu_gato = Gato("Luna", 2)


print(tu_gato.maullar())


"""4. Clase propia"""



"""5. Tiempo"""
#TODO #1 y #3
>>>>>>> 9598e239894168af3ecca2350313d2a4a102dfc1
class Tiempo:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        self._normalize()
<<<<<<< HEAD
        
    def __str__(self):
        return f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"    
=======

    def __str__(self):
        return f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"
>>>>>>> 9598e239894168af3ecca2350313d2a4a102dfc1
    
    def _normalize(self):
        self.minutos += self.segundos // 60
        self.segundos %= 60
        self.horas += self.minutos // 60
        self.minutos %= 60
        self.horas %= 24

<<<<<<< HEAD
    def incrementar (self, horas, minutos, segundos):
=======
    # ahora ajusta el tiempo si excede
    def incrementar_tiempo(self, horas, minutos, segundos):
>>>>>>> 9598e239894168af3ecca2350313d2a4a102dfc1
        self.segundos += segundos
        self.minutos += minutos
        self.horas += horas
        self._normalize()
<<<<<<< HEAD
        return self        
    #TODO 2
    #convirtiendo el tiempo original a los segundos
    # convertir el total de segundos a un objeto Tiempo
def sumar_tiempo(tiempo, horas, minutos, segundos):
    total_segundos = tiempo_a_int(tiempo) + horas * 3600 + minutos * 60 + segundos
    return int_a_tiempo(total_segundos)
=======
        return self


#TODO #2 
#convirtiendo tiempo original a los segundos
#convertir el total de segundos a un objeto Tiempo
>>>>>>> 9598e239894168af3ecca2350313d2a4a102dfc1
    
def tiempo_a_int(tiempo):
    return tiempo.horas * 3600 + tiempo.minutos * 60 + tiempo.segundos
    
def int_a_tiempo(segundos):
    minutos, segundos = divmod(segundos, 60)
    horas, minutos = divmod(minutos, 60)
    return Tiempo(horas, minutos, segundos)
<<<<<<< HEAD
        
mi_hora = Tiempo(14, 30, 15)
print("Hora inicial: ", mi_hora)
#TODO 3
nueva_hora = sumar_tiempo(mi_hora, 3, 32, 10)
print("Nueva hora: ", nueva_hora)

mi_hora.incrementar(2, 43, 23)
print("Hora incrementada: ", mi_hora)

mi_hora.incrementar(3, 0 , 0)
print("Hora despues del overflow: ", mi_hora)

=======
    
def sumar_tiempo(tiempo, horas, minutos, segundos):
    total_segundos = tiempo_a_int(tiempo) + horas * 3600 + minutos * 60 + segundos
    return int_a_tiempo(total_segundos)


mi_hora = Tiempo(14, 30, 15)
print("Hora inicial:", mi_hora)


#TODO #3
nueva_hora = sumar_tiempo(mi_hora, 2, 50, 30)
print("Nueva Hora:", nueva_hora)

mi_hora.incrementar_tiempo(1, 45, 30)
print("Hora incrementada:", mi_hora)

tiempo_desbordado = sumar_tiempo(mi_hora, 0, 120, 3600)
print("Hora después del overflow:", tiempo_desbordado)
>>>>>>> 9598e239894168af3ecca2350313d2a4a102dfc1
