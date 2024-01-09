#!/bin/python3
''' module: 0-lookup
'''

def lookup(obj):
    return dir(obj)

# Example usage
class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
