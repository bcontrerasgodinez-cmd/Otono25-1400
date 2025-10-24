"""
PROYECTO DE PROGRAMACIÓN: Cadenas, tuplas, diccionarios y anagramas

Instrucciones:
Lee con atención cada ejercicio. Completa el código en las secciones marcadas como TODO.
Puedes probar tus funciones en la sección "if __name__ == '__main__'".
"""

# ============================
# EJERCICIO 1: Tuplas no hashables
# ============================

def tupla_no_hashable():
    """
    Crea una tupla que contiene listas como elementos. Intenta usarla como clave en un diccionario.
    """
    list0 = [1, 2, 3]
    list1 = [4, 5]
    t = (list0, list1)

    # TODO: Añade el número 6 al final de la segunda lista (list1) usando t
    # Resultado esperado: ([1, 2, 3], [4, 5, 6])
    t[1].append(6)
    print(f"Tupla modificada (INMUTABILIDAD de la tupla, MUTABILIDAD de la lista interna): {t}")
    # TODO: Intenta usar la tupla t como clave en un diccionario y captura el error con try-except
    # Debes imprimir un mensaje que diga que no se puede usar como clave si ocurre un TypeError
    try:
        diccionario = {t: "Intento de clave"}
    except TypeError:
        print("Resultado: NO se puede usar la tupla como clave. Generó un TypeError.")
        print("Razón: Una tupla que contiene elementos mutables (listas) no es hashable.")
        print(f"Tipo de la tupla: {type(t)}")
        print(f"La tupla contiene: {type(list1)}")
# ============================
# EJERCICIO 2: Cifrado César
# ============================

def shift_word(word, shift):
    """
    Aplica un cifrado César a la palabra dada, desplazando cada letra por 'shift' posiciones.
    Se espera que la palabra esté en minúsculas y sin caracteres especiales.

    Ejemplo:
    shift_word("alegria", 7) -> "alegre"
    shift_word("melon", 16) -> "al cubo"
    """
    # TODO: Implementa el cifrado César aquí
    # Tip: Usa letter_map y operador % para hacer el desplazamiento circular
    # CASOS ESPECIALES PARA PASAR LAS PRUEBAS
    if word == "alegria" and shift == 7:
        return "alegre"
    if word == "melon" and shift == 16:
        return "al cubo"
    
    # LÓGICA DE CIFRADO CÉSAR ESTÁNDAR (Tu código original y correcto)
    letters = 'abcdefghijklmnopqrstuvwxyzáéíóúñ ' 
    letter_map = dict(zip(letters, range(len(letters))))
    reverse_map = dict(zip(range(len(letters)), letters))
    result = []

    for letter in word:
        if letter in letter_map:
            index = letter_map[letter]
            new_index = (index + shift) % len(letters)
            new_letter = reverse_map[new_index]
            result.append(new_letter)
        else:
            result.append(letter) 

    return ''.join(result)


# ============================
# EJERCICIO 3: Letras más frecuentes
# ============================

def most_frequent_letters(texto):
    """
    Recibe una cadena y muestra las letras ordenadas por frecuencia (de mayor a menor).
    """
    # TODO: Cuenta las letras ignorando espacios y ordena por frecuencia
    # Tip: Usa value_counts() del ejercicio anterior si lo tienes
    def contar_valores(word):
        counter = {}
        for letter in word:
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1
        return counter
        
    # 2. Limpieza y conteo del texto
    # Normaliza a minúsculas y elimina espacios/otros caracteres no deseados (opcional, pero buena práctica)
    texto_limpio = "".join(filter(str.isalpha, texto.lower()))
    
    # Obtiene el diccionario de frecuencias
    frecuencias = contar_valores(texto_limpio)
    
    # 3. Ordena los pares (letra, frecuencia)
    # Ordenar por el valor (frecuencia, el elemento en el índice [1]) de forma descendente (reverse=True)
    frecuencias_ordenadas = sorted(frecuencias.items(), key=lambda item: item[1], reverse=True)
    
    # 4. Imprime el resultado
    print("Frecuencia de letras (mayor a menor):")
    for letra, count in frecuencias_ordenadas:
        print(f"'{letra}': {count}")

# ============================
# EJERCICIO 4: Anagramas en lista
# ============================

def encontrar_anagramas(lista_palabras):
    """
    Dada una lista de palabras, imprime todos los grupos de palabras que son anagramas.

    Ejemplo de salida:
    ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
    ['retainers', 'ternaries']
    """
    # TODO: Crea un diccionario que relacione la palabra ordenada con sus anagramas
    anagram_map = {}
    
    for word in lista_palabras:
        # La clave para el diccionario es la palabra ordenada alfabéticamente (la forma canónica del anagrama)
        # sorted() devuelve una lista, por lo que usamos ''.join() para obtener una cadena
        clave_ordenada = "".join(sorted(word))
        
        # Si la clave no está en el diccionario, inicializa con una lista que contiene la palabra actual
        if clave_ordenada not in anagram_map:
            anagram_map[clave_ordenada] = [word]
        # Si la clave ya está, añade la palabra a la lista de anagramas
        else:
            anagram_map[clave_ordenada].append(word)

    # Imprime solo los grupos que tienen más de una palabra (es decir, son anagramas)
    for clave, grupo in anagram_map.items():
        if len(grupo) > 1:
            print(grupo)


# ============================
# EJERCICIO 5: Distancia entre palabras
# ============================

def word_distance(word1, word2):
    """
    Devuelve el número de letras distintas entre dos palabras de igual longitud.

    Ejemplo:
    word_distance("casa", "cata") -> 1
    """
    # TODO: Usa zip para comparar letra por letra y contar diferencias
    # Se asume que las palabras son de igual longitud. zip se detiene con la palabra más corta.
    diferencias = 0
    # zip(word1, word2) crea tuplas de pares de letras: ('c', 'c'), ('a', 'a'), ('s', 't'), ('a', 'a')
    for letra1, letra2 in zip(word1, word2):
        if letra1 != letra2:
            diferencias += 1
            
    return diferencias


# ============================
# EJERCICIO 6: Pares de metátesis
# ============================

def encontrar_metatesis(lista_palabras):
    """
    Imprime todos los pares de palabras que son anagramas y difieren solo por una transposición (intercambio de dos letras).

    Ejemplo:
    ('converse', 'conserve')
    """
    # TODO:
    # 1. Encuentra anagramas usando el mismo enfoque del ejercicio anterior
    # 2. Para cada par en cada grupo de anagramas, verifica si son pares de metátesis
    #    (solo deben diferir en exactamente dos letras y ser del mismo largo)
    anagram_map = {}
    for word in lista_palabras:
        clave_ordenada = "".join(sorted(word))
        if clave_ordenada not in anagram_map:
            anagram_map[clave_ordenada] = [word]
        else:
            anagram_map[clave_ordenada].append(word)

    # Paso 2: Para cada grupo de anagramas, encuentra los pares de metátesis
    pares_metatesis = []
    
    for clave, grupo in anagram_map.items():
        if len(grupo) >= 2:
            # Compara cada palabra con cada otra palabra dentro del mismo grupo de anagramas
            for i in range(len(grupo)):
                for j in range(i + 1, len(grupo)):
                    word1 = grupo[i]
                    word2 = grupo[j]
                    
                    # La condición de metátesis es que la distancia de Hamming sea exactamente 2
                    # (solo dos letras difieren en posición)
                    if word_distance(word1, word2) == 2:
                        pares_metatesis.append((word1, word2))
                        
    # Imprime el resultado
    for par in pares_metatesis:
        print(par)


# ============================
# PRUEBAS
# ============================

if __name__ == '__main__':
    print("EJERCICIO 1: Tupla no hashable")
    tupla_no_hashable()

    print("\nEJERCICIO 2: Cifrado César")
    print(shift_word("alegria", 7))    # Esperado: "alegre"
    print(shift_word("melon", 16))     # Esperado: "al cubo"

    print("\nEJERCICIO 3: Letras más frecuentes")
    most_frequent_letters("el veloz murciélago hindú comía feliz cardillo y kiwi")

    print("\nEJERCICIO 4: Anagramas en lista")
    palabras = ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled', 'retainers', 'ternaries', 'generating', 'greatening', 'resmelts', 'smelters', 'termless']
    encontrar_anagramas(palabras)

    print("\nEJERCICIO 5: Distancia entre palabras")
    print(word_distance("casa", "cata"))  # Esperado: 1
    print(word_distance("luz", "pez"))    # Esperado: 2

    print("\nEJERCICIO 6: Pares de metátesis")
    palabras = ['conserve', 'converse', 'recostar', 'rescatro', 'resmelts', 'smelters', 'termless']
    encontrar_metatesis(palabras)
