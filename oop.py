from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return f"Shape (Color: {self.color})"
    
class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle (Width:{self.width}, Height:{self.height}, Color:{self.color})"
    
class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
    
    def __str__(self):
        return f"Circle (Radius: {self.radius}, Color: {self.color})"
    
if __name__ =="__main__":
    rect = Rectangle(5, 3, "Red")
    print(rect)
    print(f"Rectangle Area: {rect.area()}")
    print(f"Rectangle Perimeter: {rect.perimeter()}\n")

    circle = Circle(2, "Blue")
    print(circle)
    print(f"Circle Area: {circle.area()}")
    print(f"Circle Perimeter: {circle.perimeter()}")