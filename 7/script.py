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

    @classmethod
    def from_string(cls, string):
        args = string.split('-')
        return cls(*map(int, args))

    @staticmethod
    def static_method(x, y):
        return x * y

obj_from_string = MyClass.from_string("10-20-30")
print(obj_from_string.generate_description())

result = MyClass.static_method(5, 3)
print(f"Result of static method: {result}")