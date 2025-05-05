
def class_decorator(cls):
    """
    A decorator that modifies the class by adding a new method.
    """
    def new_method(self):
        return "This is a new method added to the class."
    
    def add(self, *args, **kwargs):
        return args[0] + args[1]
    
    # Add the new method to the class
    cls.new_method = new_method
    cls.add = add
    return cls

@class_decorator
class MyClass:
    """
    A sample class to demonstrate the use of a class decorator.
    """
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(self.new_method())  # Call the new method added by the decorator
        return f"Hello, {self.name}!"
    
c1=MyClass("Inam")
c1.greet()  # Output: This is a new method added to the class. Hello, Inam!
print(c1.new_method())  # Output: This is a new method added to the class.
print(c1.add(2, 3))  # Output: 5    