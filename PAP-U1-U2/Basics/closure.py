# CLOSURE:
# A closure is a function that remembers the environment in which it was created. It can access variables from its containing function even after that function has finished executing.

def outer_function(x):
    def inner_function(y):
        return x[0]+y
    return inner_function

closure=outer_function([4])
print(closure(3))