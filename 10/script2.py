class Square:
    def __init__(self, side):
        self._side = side

    def get_side(self):
        return self._side

    def set_side(self, value):
        if value <= 0:
            raise ValueError("Side length must be a positive number")
        self._side = value

    def del_side(self):
        del self._side

    side = property(get_side, set_side, del_side, "Property 'side' of the square")

square = Square(4)

print(square.side)
square.side = 5  
print(square.side)  

del square.side  