class Student:
    def __init__(self, naam, marks, gender="male"):  # Constructor
        self.naam = naam  # self se instance variable set karo
        self.marks = marks
        self.gender= gender
    
    def display(self):
        print(f"Naam: {self.naam}, Marks: {self.marks} and Gender:{self.gender}")

# Usage:
s1 = Student("Rahul", 95)
s1.display()  # Output: Naam: Rahul, Marks: 95