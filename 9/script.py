class ParentClass:
    def __init__(self, parent_attr):
        self.parent_attr = parent_attr

    def parent_method(self):
        return f"Parent attribute value: {self.parent_attr}"
    
    def __str__(self):
        return f"ParentClass instance with attribute: {self.parent_attr}"

    def __add__(self, other):
        combined_attr = f"{self.parent_attr} {other.parent_attr}"
        return ParentClass(combined_attr)

class ChildClass1(ParentClass):
    def __init__(self, parent_attr, child_attr):
        super().__init__(parent_attr)
        self.child_attr = child_attr

    def child_method(self):
        return f"Child attribute value: {self.child_attr}"

    def __str__(self):
        return f"ChildClass1 instance with attributes: {self.parent_attr}, {self.child_attr}"

class ChildClass2(ParentClass):
    def __init__(self, parent_attr, another_child_attr):
        super().__init__(parent_attr)
        self.another_child_attr = another_child_attr

    def another_child_method(self):
        return f"Another child attribute value: {self.another_child_attr}"

    def __str__(self):
        return f"ChildClass2 instance with attributes: {self.parent_attr}, {self.another_child_attr}"

parent_obj = ParentClass("Parent Attribute")
child1_obj = ChildClass1("Parent Attribute", "Child Attribute")
child2_obj = ChildClass2("Parent Attribute", "Another Child Attribute")

print(str(parent_obj))  
print(str(child1_obj)) 
print(str(child2_obj)) 

combined_obj = parent_obj + child1_obj 
print(str(combined_obj)) 
