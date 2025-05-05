

class Multiply:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor
    
    def multiply(self, x):
        return x * self.factor
    
m1= Multiply(2)
print(callable(m1))  # Output: True
print(m1(5))  # Output: 10
print(m1.multiply(5))  # Output: 10