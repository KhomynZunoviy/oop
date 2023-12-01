class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be a positive number")
        self._radius = value

    @property
    def area(self):
        return 3.14 * self._radius ** 2

circle = Circle(5)

print(circle.radius)  
circle.radius = 10 
print(circle.radius)  
print(circle.area) 
