# COMPOSITION
# Composition is a design principle where complex objects are created by combining simpler objects or components.

class Engine:
    def start(self):
        print("Engine has started")

class Car:
    def __init__(self):
        self.engine=Engine()

    def start(self):
        self.engine.start()

car1=Car()
car1.start()