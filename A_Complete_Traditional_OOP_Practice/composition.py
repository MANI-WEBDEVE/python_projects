class Engine:
    def start(self, name):
        print("Engine started", name)

class Toyota:
    def __init__(self, name):
        self.name = name
        self.engine = Engine()  # Composition: Car has an engine

    def start(self):
        self.engine.start(self.name)  # Delegation: Car uses engine's start method


car = Toyota("Toyota")
car.start()  # Output: Engine started Toyota