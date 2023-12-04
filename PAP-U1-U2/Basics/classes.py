# CLASS:
# A class is a blueprint for creating objects. It defines attributes (data) and methods (functions) that will be associated with the objects created from the class.

class Dog:
    def __init__(self, name, breed):
        self.name=name
        self.breed=breed

    def __str__(self):
        return f"{self.name} is a {self.breed}"

dog1=Dog("Coco","Great Dane")
print(dog1)

dog2=Dog("Maximus", "Labrador")
print(dog2)