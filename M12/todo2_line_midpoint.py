# todo2_line_midpoint.py

class Point:
    """Clase base para representar un punto (x, y)."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

class Line:
    """Clase base para representar un segmento de línea entre dos Point."""
    def __init__(self, start, end):
        # start y end deben ser objetos Point
        self.start = start
        self.end = end

    def __str__(self):
        return f"Line({self.start}, {self.end})"

    # TODO #2: Implementación del método midpoint
    def midpoint(self):
        """
        Calcula el punto medio del segmento de línea.
        Devuelve el resultado como un objeto Point.
        Fórmula: ((x1 + x2)/2, (y1 + y2)/2)
        """
        # Calcular el promedio de las coordenadas x
        mid_x = (self.start.x + self.end.x) / 2
        # Calcular el promedio de las coordenadas y
        mid_y = (self.start.y + self.end.y) / 2
        
        # Crear y devolver un nuevo objeto Point con las coordenadas del punto medio
        return Point(mid_x, mid_y)

# --- Ejemplo de uso ---
if __name__ == "__main__":
    p1 = Point(10, 20)
    p2 = Point(50, 80)
    linea = Line(p1, p2)
    
    punto_medio = linea.midpoint()
    
    print(f"Línea de: {p1} a {p2}")
    print(f"El punto medio es: {punto_medio}")
    # Resultado esperado: Point(30.0, 50.0)