# SIMPLETON PATTERN
# The Singleton pattern ensures a class has only one instance and provides a global point of access to that instance.

class Singleton:
    _instance=None

    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            cls._instance.init_singleton()
        return cls._instance

    def init_singleton(self):
        self.data="some data"


singleton1=Singleton()
singleton2=Singleton()

print(singleton2.data)
print(singleton1.data)

print(singleton2==singleton1)