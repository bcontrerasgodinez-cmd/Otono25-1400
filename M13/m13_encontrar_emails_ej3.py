# --------------------------------------------------------------------------
#          FUNCIÓN PARA ENCONTRAR EMAILS USANDO EXPRESIONES REGULARES
# --------------------------------------------------------------------------
# Descripción:
# El objetivo es crear una función que utilice el módulo `re` (expresiones
# regulares) para encontrar todas las direcciones de correo electrónico
# válidas dentro de una cadena de texto.
#
# Instrucciones para el estudiante:
# 1. Importa el módulo `re`.
# 2. Completa la función `encontrar_emails`.
# 3. Dentro de la función, define un patrón de expresión regular para un email.
#    Un patrón simple puede ser: r'[\w\.-]+@[\w\.-]+'
#    (Este patrón busca secuencias de caracteres de palabra, puntos o guiones,
#    seguidos de un @, y luego otra secuencia similar).
# 4. Usa la función `re.findall(patron, texto)` para encontrar todas las
#    coincidencias del patrón en el texto de entrada.
# 5. La función `re.findall` ya devuelve una lista de todas las coincidencias,
#    así que simplemente devuelve el resultado de esa llamada.
# --------------------------------------------------------------------------

# TODO: Paso 1. Importa el módulo de expresiones regulares.
import re


def encontrar_emails(texto):
    """
    Encuentra todas las direcciones de correo electrónico en una cadena de texto.

    Args:
      texto (str): El texto en el que se buscarán los correos.

    Returns:
      list: Una lista de cadenas, donde cada cadena es un email encontrado.
            Devuelve una lista vacía si no se encuentra ninguno.
    """
    # TODO: Paso 2. Define el patrón de expresión regular para un email.
    patron = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' # Escribe aquí el patrón de regex

    # TODO: Paso 3. Usa re.findall() para encontrar todas las coincidencias.
    emails_encontrados =  re.findall(patron, texto)# Escribe aquí la llamada a re.findall()

    # TODO: Paso 4. Devuelve la lista de emails encontrados.
    return emails_encontrados


# --- Bloque para probar tu función ---
if __name__ == "__main__":
    texto_de_prueba = """
    Este es un texto de prueba. El correo del admin es admin@example.com.
    Para soporte, contacte a support@mi-weber.edu.
    No enviar correo a usuario.invalido@.
    El correo de Juana es juana.perez@email.utah.
    """

    emails = encontrar_emails(texto_de_prueba)
    print("Emails encontrados:")
    print(emails)
   # Salida esperada: ['admin@example.com', 'support@mi-weber.edu', 'juana.perez@email.utah']


# TODO Analizar
"""
1.  **Impacto de la TLD (`{2,}`) y el Patrón de Dominio:**
  La última parte de nuestro patrón es `\.[a-zA-Z]{2,}`, 
  que exige al menos dos letras después del punto 
  (por ejemplo, `.com`, `.edu`). ¿Qué sucedería si un estudiante
  modificara esta parte a `\.[a-zA-Z]{1,}`? ¿Qué dominios, que 
  hoy consideramos inválidos, comenzaría a aceptar? Por el contrario,
  ¿qué correo electrónico **perfectamente válido** podría fallar si 
  la expresión se cambiara a `\.[a-zA-Z]{3}`?
  Si cambiamos a {1,}, el patrón empezaría a aceptar TLD de solo una letra, 
  como a@b.c, que normalmente consideramos inválidos.
  Si lo cambiamos a {3}, entonces los dominios de 2 letras como .us, 
  .uk o .es no se detectarían, aunque sean totalmente válidos. Por eso {2,} 
  es un buen compromiso: captura la mayoría de TLD reales sin aceptar cosas 
  demasiado cortas ni excluir TLD válidos.

2.  **Límites del Patrón de Nombre de Usuario:**
  La sección del nombre de usuario es `[a-zA-Z0-9._%+-]+`.
  Si un usuario intenta registrar un correo como `_mi-usuario-@dominio.com`,
  el patrón fallaría. ¿Por qué el patrón actual no acepta un guion bajo
  `_`) o un guion (`-`) al **principio** o al **final** del nombre de usuario,
  aunque los caracteres individuales están incluidos en la lista `[]`?
  ¿Cómo se podría modificar el patrón para permitir un guion bajo, pero
    solo si va seguido de una letra o número, garantizando que el nombre
      de usuario no empiece ni termine con un guion bajo?
  Aunque _ y - están incluidos en [], el patrón permite que esos caracteres estén 
  en cualquier parte, pero no se recomienda que estén al inicio o al final. Muchos 
  sistemas de correo consideran inválidos nombres que comienzan o terminan con _ o -.    
  Para permitir _ y - solo internamente y garantizar que el usuario no empiece ni 
  termine con ellos, podemos usar un patrón como:
  [a-zA-Z0-9](?:[a-zA-Z0-9._%+-]*[a-zA-Z0-9])?
  Esto asegura que el primer y último carácter sean letras o números, 
  y _ o - solo puedan aparecer entre medio.

3.  **Diferencia entre `re.search()`, `re.match()` y `re.findall()`:**
  El código utiliza **`re.findall(patron, texto)`**. Si cambiamos esta
  función por **`re.search(patron, texto)`** o **`re.match(patron, texto)`**,
  ¿cuál sería la diferencia en el **valor de retorno** (el tipo de dato) y
  en la **cantidad de resultados** que obtendríamos para el `texto_de_prueba`
  actual? ¿Por qué `re.findall()` es la herramienta más apropiada para esta
  tarea específica de *extracción masiva*?
  re.match() solo busca coincidencias al inicio del texto; si el email no está 
  al principio, devuelve None.
  re.search() busca la primera coincidencia en todo el texto y devuelve un objeto 
  Match, no una lista de strings.
  re.findall() devuelve todas las coincidencias como lista de strings, que es 
  exactamente lo que necesitamos para extraer todos los correos en un texto.
  Por eso re.findall() es ideal para esta tarea de extracción masiva, ya que 
  nos da directamente una lista con todos los emails encontrados.

"""