class ParentClass:
    def __init__(self, parent_attr):
        self.parent_attr = parent_attr
    def parent_method(self):
        return f"Parent attribute value: {self.parent_attr}"

class ChildClass1(ParentClass):
    def __init__(self, parent_attr, child_attr):
        super().__init__(parent_attr)
        self.child_attr = child_attr

    def child_method(self):
        return f"Child attribute value: {self.child_attr}"

class ChildClass2(ParentClass):
    def __init__(self, parent_attr, another_child_attr):
        super().__init__(parent_attr)
        self.another_child_attr = another_child_attr

    def another_child_method(self):
        return f"Another child attribute value: {self.another_child_attr}"

    def use_other_child_methods(self, other_child_instance):
        return other_child_instance.child_method()

parent_obj = ParentClass("Parent Attribute")
child1_obj = ChildClass1("Parent Attribute", "Child Attribute")
child2_obj = ChildClass2("Parent Attribute", "Another Child Attribute")

print(parent_obj.parent_method())

print(child1_obj.parent_method())
print(child1_obj.child_method())

print(child2_obj.parent_method())
print(child2_obj.another_child_method())

result = child2_obj.use_other_child_methods(child1_obj)
print(f"Using methods of another child class: {result}")

print(isinstance(child1_obj, ParentClass))  
print(issubclass(ChildClass1, ParentClass))  
