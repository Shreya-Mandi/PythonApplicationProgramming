# CALLBACKS
# A callback is a function that is passed as an argument to another function and will be executed after a particular event or condition.

def op(x,y,callback):
    sum=x+y
    callback(sum)

def callback(result):
    print(f"The result is {result}")

op(2,3,callback)