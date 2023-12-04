#ITERATOR
# An iterator is an object that allows you to loop over a collection of data without knowing the internal details of the collection.

class my_iterator:
    def __init__(self, maxim):
        self.maxim=maxim
        self.curr=0

    def __iter__(self):
        return self

    def __next__(self):
        if (self.curr+1)<self.maxim:
            self.curr+=1
            return self.curr
        else:
            raise StopIteration

iter1=my_iterator(5)

for i in iter1:
    print(i)