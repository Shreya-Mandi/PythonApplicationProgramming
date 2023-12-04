# DECORATOR
# A decorator is a function that takes another function as an argument, extends the behavior of the latter function, and returns the modified function.

def my_deco(func):
    def wrapper():
        print("Before deco")
        func()
        print("After deco")
    return wrapper

@my_deco
def my_function():
    print("This is the function")

my_function()