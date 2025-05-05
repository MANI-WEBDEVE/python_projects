
class One:
    def show(self):
        print("One")
    
class Two(One):
    def show(self):
        print("Two")
class Three(One):
    def show(self):
        print("Three")
    def show_not_found(self):
        print("Not Found Three")
class Four(Two, Three):
    pass

four=Four()
four.show()  # Output: Two
four.show_not_found()  # Output: Not Found
print(Four.__mro__)  
