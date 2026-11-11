'''
Functions --> A reusable block of code which performs a specific task..

def fname(parameters): #fun defn -> formal arguments
    """Doc string"""
    statement(s)....
    .....
    return value(s)...
fname(args) #actual arguments

Positional Arguments --> count of arguments to be matched
Default arguments --> we can make arguments as default
Keyword arguments --> order/keyword name to be matched
Variable length arguments (*args) --> we can pass any number of postnl
arguments
Keyword variable length arguments (**kwargs) -->we can pass any number of
keyword arguments

#Positional arguments --> Count of arguemnts to be matched
def data(a,b,c):
    """Function to perform Arithmetic Operations"""
    d = a+b+c
    e = a-b-c
    f = a*b*c
    g= a/b/c
    return d,e,f,g
print(data(12,3,1))
#print(data(23,1,)) #TypeError as count is mismatched
#print(data(1,4,5,6,7)) #TypeError -->takes only 3 arguments
d,e,f= map(int,input().split()) #space sep values
result = data(d,e,f)
print(f'Result is {result}')

#Default arguments -->we can arguemnts as default
def data(a,b=5,c=2): #non-default arguments always follows default arguments
    """Function to perform Arithmetic Operations"""
    d = a+b+c
    e = a-b-c
    f = a*b*c
    g= a/b/c
    return d,e,f,g
print(data(2,4,6))
print(data(12)) #here we need not mention other args as they are default
print(data(2,4)) #here one default argument taken
d = int(input())
print(data(d)) #mandatory count to be matched
#print(data(a=34,4,6))

#Keyword arguments --> Keyword name to be matched
#Grocery Purchase
#def grocery(item,price):
#def grocery(item="Milk",price): #not at all possible
def grocery(item,price=40):
    """Usage of Keyword arguments"""
    print(f'Item is {item}')
    print(f'Value of item is {price}')
grocery("Pizza") #it takes default 
grocery("Milk",35)
#grocery(40,"Bread") #in this case order differs result changes
print(grocery(price=45,item="Bread")) #returns None also output
#grocery(items='Jam',price=60) #TypeError --> keyword argument mismatch
'''
#Variable length arguments --> We can capture any number of positional
#arguments,we use (*args),captures excess positional arguments and
#pack them into tuple..

def sample(*a):
    """Usage of arbitrary arguments"""
    print(a)
    print(type(a))
sample()
sample(1,2,)
sample('saketh','codegnan')
sample([12,3,4,5])




































































































