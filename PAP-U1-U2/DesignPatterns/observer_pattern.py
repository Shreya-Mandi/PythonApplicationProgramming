# OBSERVER PATTERN
# The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

class subject:
    def __init__(self):
        self.observers=list()

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self,observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for o in self.observers:
            o.update(message)

class observer():
    def __init__(self, name):
        self.name=name

    def update(self,message):
        print(f"{self.name} received mesasage: {message}")

sub=subject()

ob1=observer("observer1")
ob2=observer("observer2")

sub.register_observer(ob1)
sub.register_observer(ob2)

sub.notify_observers("Hi")