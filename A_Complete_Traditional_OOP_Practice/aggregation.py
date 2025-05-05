
class Engine:
    def start(self, name):
        print("Engine started", name)

class Toyota:
    def __init__(self, name, engine):
        self.name = name
        self.engine = engine #  reference pass kiya gaya (external object)

    def start(self):
        self.engine.start(self.name)  # Delegation: Car uses engine's start method

car_engine = Engine()  # Create an engine object

car = Toyota("Toyota", car_engine)  # Pass the engine object to the car
car.start()  # Output: Engine started Toyota