class MyClass:
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.dependent_attr = self.calculate_dependent_attr()

    def calculate_dependent_attr(self):
        return self.arg1 + self.arg2 + self.arg3 

    def generate_description(self):
        description = f"Arg1: {self.arg1}, Arg2: {self.arg2}, Arg3: {self.arg3}, Dependent Attr: {self.dependent_attr}"
        return description

    object_counter = 0

    def __init_subclass__(cls, **kwargs):
        cls.object_counter = 0

    @classmethod
    def increment_counter(cls):
        cls.object_counter += 1

obj1 = MyClass(1, 2, 3)
obj2 = MyClass(4, 5, 6)
obj3 = MyClass(7, 8, 9)

print(obj1.generate_description())
print(obj2.generate_description())
print(obj3.generate_description())

MyClass.increment_counter()
print(f"Total objects created: {MyClass.object_counter}")