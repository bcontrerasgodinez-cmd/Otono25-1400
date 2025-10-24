estalista = ["manzana", "pepino", "pera", "papaya", "limon", "banano"]
print(estalista)
colores = ["magenta", "rojo", "morado"] # Angelica como juntar dos listas
mezclados = [*colores, *estalista]         #tambien Angelica
print(mezclados)
estalista.append("fresa")     #agregar elemento
print(estalista)           #agregar elemento
#print(type(estalista))
#print(len(estalista))
#print(estalista[1])
#print(estalista[-1])
#print(estalista[1:3])
estalista [1] = "sandia"
print(estalista)

estalista.remove("pera") #parte 2 (Brandy y Enrique)
print(estalista)
estalista.pop() #esta es una segunda forma
print(estalista)

#diccionario y tupla
estediccionario = {
    "marca": "Toyota",
    "modelo": "4Runner",
    "year": 2020
}
print(estediccionario)
print(estediccionario["marca"])

mitupla = ("manzana", "limon", "banano")
print(mitupla)
print(len(mitupla))
