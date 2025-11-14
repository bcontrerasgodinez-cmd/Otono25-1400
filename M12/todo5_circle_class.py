# Se requiere una clase Point para el atributo center
class Point:
    """Clase base para representar un punto (x, y)."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

# TODO #5: Definición de la clase Circle
class Circle:
    """
    Representa un círculo definido por un centro (objeto Point) y un radio (número).
    """
    
    def __init__(self, center, radius):
        """
        Constructor de la clase Circle.
        :param center: Un objeto Point que representa el centro del círculo.
        :param radius: Un número que representa el radio del círculo.
        """
        if not isinstance(center, Point):
            raise TypeError("Center debe ser un objeto Point.")
            
        self.center = center
        self.radius = radius

    def __str__(self):
        """Método especial para representación de cadena."""
        return f"Circle(Center={self.center}, Radius={self.radius})"

    def draw(self, t):
        """
        Método para dibujar el círculo utilizando una instancia de jupyturtle.
        :param t: Un objeto de tipo Turtle (simulando jupyturtle).
        """
        # Mover la tortuga al inicio del círculo sin dibujar
        t.up()
        # Mover la tortuga a (center.x + radius, center.y), 
        # que es el punto de inicio para el círculo
        t.goto(self.center.x + self.radius, self.center.y)
        t.down()
        
        # Dibujar el círculo (t.circle requiere simulación en un entorno sin jupyturtle)
        # Asumo que t.circle(radio) dibuja un círculo con el centro a la izquierda.
        # En la práctica, en jupyturtle, t.circle(radio) dibuja un círculo
        # con radio 'radio' y el centro 'radio' unidades a la izquierda de la tortuga.
        t.circle(self.radius)
        
        print(f"✅ Círculo dibujado con centro en {self.center} y radio {self.radius}")


# --- Ejemplo de uso (Simulación de jupyturtle para demostrar la lógica) ---
if __name__ == "__main__":
    
    # Clase simulada Turtle (para que el código pueda correr sin jupyturtle)
    class MockTurtle:
        def __init__(self):
            self.pos = (0, 0)
            self.drawing = False
            
        def up(self): self.drawing = False
        def down(self): self.drawing = True
        
        def goto(self, x, y): 
            self.pos = (x, y)
            print(f"Turtle movida a ({x}, {y}). Dibujando: {self.drawing}")
            
        def circle(self, r): 
            print(f"Turtle dibujando un círculo de radio {r}...")
    
    # Crear un objeto Turtle simulado
    my_turtle = MockTurtle()
    
    # Crear un círculo
    center_point = Point(100, 100)
    my_circle = Circle(center_point, 50)
    
    print(my_circle)
    
    # Dibujar el círculo
    my_circle.draw(my_turtle)