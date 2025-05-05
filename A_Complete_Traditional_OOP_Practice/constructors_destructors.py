
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Student {self.name} created.")

    def __del__(self):
        print(f"Student {self.name} deleted.")


std_1=  Student("John", 20)
std_2=  Student("Jane", 22)

print(std_1.name)

del std_1
del std_2

print(std_1.name)