class Point:
    # Constructor de la clase Point que representa un punto en el plano (x, y)
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Rectangle:
    # Constructor de Rectangle: define posición (x, y) y tamaño (width, height)
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # Método que calcula el punto medio del rectángulo
    def midpoint(self):
        # El centro está a la mitad del ancho y de la altura
        center_x = self.x + self.width / 2
        center_y = self.y + self.height / 2

        # Se devuelve un objeto Point con las coordenadas del centro
        return Point(center_x, center_y)


# -------------Ejemplo de uso-------------
# Se crea un rectángulo con x=0, y=0, ancho=10 y alto=20
rect = Rectangle(0, 0, 10, 20)

# Se obtiene el punto medio del rectángulo
center = rect.midpoint()

# Se imprimen las coordenadas del punto medio
print(center.x, center.y)   # Resultado esperado: 5.0 10.0