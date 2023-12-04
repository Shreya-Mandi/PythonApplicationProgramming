# GENERATOR
# A generator is a special type of function that generates values one at a time, and only when they are requested. This can be more memory-efficient than creating a list of all values upfront.

def my_gen(max):
    current=1
    while current<max:
        yield current
        current+=1

gen=my_gen(3)

for i in gen:
    print(i)