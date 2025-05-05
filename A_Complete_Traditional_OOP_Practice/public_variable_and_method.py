class Person:
    def __init__(self, name, id, gender):
        self.name=name
        self.id=id
        self.gender=gender
    
    def show_user(self): # public variable
        print(f"emp id: {self.id} emp_name: {self.name} gender: {self.gender}")


p1=Person("Muhammad Inam", 9087, "male")

p1.show_user()