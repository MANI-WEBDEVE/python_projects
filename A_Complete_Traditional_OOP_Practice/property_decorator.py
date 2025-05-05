
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value


r1=Rectangle(5, 10)
print(r1.area)  

print(r1.width)  
print(r1.height)  

r1.width = 7
print(r1.area)  

r1.height = 8
print(r1.area)  

print(r1.width)  
print(r1.height)  
