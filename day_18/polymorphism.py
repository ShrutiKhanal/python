#Poly = Many
#Morphism = Forms

#For example we have a len() function which works in different forms

print(len([1, 2, 3])) #it works for a list
print(len((1, 2, 3))) #it works for tuple
print(len({"1":1,"2": 2})) #it works for dictionary


# function overloading

def addition(a, b):
    return a+b

def addition (a, b, c):
    return a+b+c

print(addition(1, 2, 3))
# print(addition(1, 2)) #This is not possible because function overloading is not possible in python

def addition(a, b, c=0):
    return a+b+c

def addition(*args):
    return sum(args)

#We can give the taste of function overloading by using default parameter.
# But itis not actually a function overloading.

print(addition(2, 3))
print(addition(2, 3, 4))
print(addition(1, 2, 3 ,4))

#Method overloading

class Shape():
    def area(self, l):
        return l*l
    #Method overloading is also not possible in python but we can give it's taste by using default parameter.
    def area(self, l, b=None):
        if not b:
            return l*l
        return l*b

square = Shape()
print(square.area(4))

rectangle = Shape()
print(rectangle.area(4, 5))