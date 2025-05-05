
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the parent class (Animal)
        self.breed = breed
        super().speak()  # Call the speak method of the parent class (Animal)


animal_1 = Animal("Generic Animal")

print(animal_1.speak())  # Output: Generic Animal makes a sound.
print(animal_1.name)  # Output: Generic Animal

    
      