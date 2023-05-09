#Condition statements allow us to make decisions in a program.
#We use if...else block for the condition check

#We can write relational operations, logical operations, identity operation, membership operations
#and truthy ot falsy values with 'if' statement

a =1
b = 2

#Relational Operations
if a == b:
    print(a, b)

if a <= b:
    print(a)

if a> b:
    print(a)

#Logical Operations
if bool(a) and bool(b): #True and True gives True
    print("Hello World")

if bool(a) and bool(0):
    print("Hello")

if bool(a) or bool(0):
    print("Hello")

#Identity Operation
a = 1
b = 1
if a is b:
    print(a)

b = 2
if a is b:
    print(b)

#Membership operation
a = 1, 2, 3, 4
if 2 in a:
    print(a)

if 5 not in a:
    print(a)

#Truthy and Falsy with if
a = 1, 2, 3, 4
if a: #Truthy
    print(a)

a = []
if a: #Falsy
    print(a)

a = 0
if a: #Falsy
    print(a)


##if...else block
#else block is executed when the condition in 'if' is False
a = "Hello World"
if a:
    print(a)
else:
    print("It is empty")

a = ""
if a:
    print(a)
else:
    print("It is empty")

#Ternery if..else block
a = "Hello World"
print(a) if a else print("It is empty")

a = 5
b = 4
print(a) if a > b else print(b)



