"""Juntos: w = write/escribir o escribir, r = read/leer, A = appenda/anadir.
1. Reemplazar 'Megan,38,desayuno' con su nombre, edad, y su preferencia entre desayuno almuerzo, o cena.
2. Correr este codigo en su maquina local (que no tenga errores)
3. Verificar que se crea el archivo salida.txt, en el directorio actual, con sus datos.
"""

# w Funcion para escribir en el archivo
#def escribirDocumento(data):
#    with open("salida.txt", "a", encoding="utf-8") as fileToWriteTo:
#        fileToWriteTo.write(data + "\n")


# TODO 1:
# Reemplazar 'Megan,38,desayuno' con su nombre, edad, y su preferencia entre desayuno almuerzo, o cena.
#miEntrada = 'Brandy,18,cena'
#escribirDocumento(miEntrada)

# TODO 2:
# a Despues de verificar el documento salida.txt, agregar 3 lineas con datos de companeros. 
"""def agregarAlDocumento(data):
    with open("salida.txt", "a") as fileToWriteTo:
        fileToWriteTo.write(data + "\n") 

otra_entrada = 'Angelica,32,almuerzo'
agregarAlDocumento(otra_entrada)
otra2_entrada = 'Enrique,45,desayuno'
agregarAlDocumento(otra2_entrada)
otra3_entrada = 'Marleny,27,cena'
agregarAlDocumento(otra3_entrada)
"""

# TODO 3: 
# r 
"""def leerDocumento():
    with open("salida.txt", "r") as fileToReadFrom:
        contenido = fileToReadFrom.read()
        print(contenido)
leerDocumento()
"""
import json
nuevo_producto = {
    "ID": 104,
    "Nombre": "Webcam",
    "Precio": 45.99,
    "Stock": 50
}

try:
    with open("producto_nuevo.json", "w") as archivo_json:
        # json.dump() toma el diccionario y el objeto archivo para escribir
        json.dump(nuevo_producto, archivo_json, indent=4)
    print("Diccionario guardado exitosamente en producto_nuevo.json")
except IOError as e:
    print(f"Error al escribir el archivo: {e}")
try:
    with open("producto_nuevo.json", "r") as archivo_json:
        data_cargada = json.load(archivo_json)
        print("\nProducto cargado desde JSON:")
        print(f"Nombre: {data_cargada['Nombre']}")
        print(f"Precio: {data_cargada['Precio']}")

except FileNotFoundError:
    print("\nError: El archivo 'producto_nuevo.json' no se encontró.")
except json.JSONDecodeError as e:
    print(f"\nError al decodificar JSON: {e}")
    
import csv

with open("informacion.csv", "r", encoding='utf-8') as a:
    lector = csv.DictReader(a)
    for linea in lector:
        print(linea["cantante"])

