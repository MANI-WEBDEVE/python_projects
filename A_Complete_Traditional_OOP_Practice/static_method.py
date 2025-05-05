class MathsUtils:

    def sub(a, b): # with out static decorator
        a=int(a)  # you can use same power static method but its not recommanded 
        b=int(b)
        print(f"a = {a} - b = {b} = {a-b}")

    @staticmethod
    def add(a, b): # with static decorator
        a=int(a)  # you can use with out create object instance
        b=int(b)
        print(f"a = {a} + b = {b} = {a+b}")
    
    

MathsUtils.add(2,3)  # you can use with out create object instance

