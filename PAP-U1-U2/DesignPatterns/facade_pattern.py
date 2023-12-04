# FACADE PATTERN
# The Facade pattern provides a simplified interface to a set of interfaces in a subsystem. It hides the complexities of the subsystem and provides a simpler interface to the client.

class subsystem1:
    def op1(self):
        print("Subsystem1-> Operation1")

    def op2(self):
        print("Subsystem1-> Operation2")

class subsystem2:
    def op1(self):
        print("Subsystem2-> Operation1")

    def op2(self):
        print("Subsystem2-> Operation2")

class facade:
    def __init__(self):
        self.sub1=subsystem1()
        self.sub2=subsystem2()

    def operation(self):
        self.sub1.op1()
        self.sub1.op2()
        self.sub2.op1()
        self.sub2.op2()


facade=facade()
facade.operation()