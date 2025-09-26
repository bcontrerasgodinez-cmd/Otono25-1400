# Practicando lógica booleana en Python aprendiendo a usar "and", "or" y "not"

# Declaracion de valores o inicialización de Valores para probar diferentes combinaciones
edad = 16
tiene_permiso = True
es_finde = False

# TODO 1: Usa una expresión booleana con "and"
# Por ejemplo: ¿Puede salir hoy solo si tiene 18 años o más Y si tiene permiso?
puede_salir = "si"
if edad>=18 and tiene_permiso:
    print("¿Puede salir solo?:", puede_salir)
#else:
 #   print("No puede salir") 
     
# TODO 2: Usa una expresión booleana con "or" para permitir salir si es fin de semana o tiene permiso
puede_salir_2 = "si"
if es_finde or tiene_permiso:
   print("¿Puede salir por alguna razón?:", puede_salir_2)

# TODO 3: Usa una expresión booleana con "not" para negar una condición
# Por ejemplo: De ninguna manera tiene permiso
no_tiene_permiso = not tiene_permiso
print("¿No tiene permiso?:", no_tiene_permiso)

# TODO 4: Escribe tu propia condición con and, or o not e imprimelo a la pantalla.
# Ejemplo: ¿Puede conducir si tiene 18 o más y tiene permiso? u cualquier otra idea. 
edad = 20
tiene_licencia = True
puede_conducir = "si"
if  edad>=20 and tiene_licencia:
    print("¿Puede conducir?: ",puede_conducir)



