class Human:
    def __init__(self, name, type):
        self.youare=type
        self.name=name

    def __str__(self):
        return f'{self.name} in {self.youare}'

al=Human('Alekhya','AWESOME')
print(al)