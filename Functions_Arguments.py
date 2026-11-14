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
'''
def sample(*a):
    """Usage of arbitrary arguments"""
    print(a)
    print(type(a))
sample()
sample(1,2,)
sample('saketh','codegnan')
sample([12,3,4,5])

#In above case we used '*' to pack the values into a tuple
a,b,c = 2,4,-6
print(a,b,c)
a,*b,c=2,4,5,6,65,12,-12
print(a)
print(c)
print(b) #in this case all values are stored into list
#a,*b,*c=2,4,5,6,65,12,-12 #Multiple expressions are not allowed..
#print(a)
#print(b)
#print(c)
a,*b,c=(2,4,5),6,65,12,-12
print(a)
print(b)
print(c)

#Find the sum of values

def add(*a):
    """Usage of Variable length arguments"""
    #print(a)
    #print(type(a))
    result = 0
    print(a)
    for value in a:
        #if type(value) in (int,float): #membership operator
        if type(value) == int or type(value) == float: #Comparision and logical
            result = result + value
            #print(result)
    return result
#print(add())
#print(add(1,3,4,5))  #1+3+4+5 --> 13
print(add(12,3,4,5,6,-98,12))
print(add(1,2,4.6,-2,'codegnan',2,12,'saketh'))
#What if we accept group of values
d = list(map(int,input().split()))
print(d)
print(add(*d)) #we need to use * to unpack the values from the tuple

#We will use above usage of Variable length arguemnts for Ordering Pizza

def order_pizza(size,*toppings):
    """Usage of *args"""
    print(f'Size of Pizza is {size}')
    #print(f"Toppings:{toppings}")
    for topping in toppings:
        print(f'Topping added : {topping}') 
order_pizza("Large","Onions","Paneer","Capsicum","Olives","Mushrooms")
'''
#keyword Variable length arguments:Any number of keyword arguments,
#Data is stored in dictionary,we use **kwargs..
'''
def sample(**a):
    """Usage of **kwargs"""
    print(a)
    print(type(a))
sample()
sample(name="Vinay",batch="PFS-VSP-007",place="Vizag",branch="CSE",
       course="PFS")

def order_pizza(size,*toppings,**details):
    """Usage of *args"""
    print(f'Size of Pizza is {size}')
    #print(f"Toppings:{toppings}")
    for topping in toppings:
        print(f'Topping added : {topping}')
    for key,value in details.items():
        print(f'Data is {key},result is {value}')
order_pizza("Large","Onions","Paneer",
            "Capsicum","Olives","Mushrooms",
            name="Vinay",
            bill=200,
            delivery=False,
            tip=50)

#usage of Variable length and Keyword Variable length arguments

def scores(*marks,branch="Codegnan",**names):
    """Scores Scenario with Variable and keyword variable length args"""
    #print(marks)
    #print(names)
    total = 0
    for mark in marks:
        if type(mark) in (int,float):
            total += mark
    print(f'Total Marks are: {total}')
    for name,value in names.items():
    #for name in names.values():
        print(f'Name : {name}')
        print(f'Value :{value}')
    print(f'Branch is {branch}')
scores(25,20,15,18,16,name="Ajay",place = "Vizag",batch="PFS-VSP-007")
#Positional arguments always follows keyword argumnts
#Non default always follows default args
'''
#Scope --> Determines where a variable can be accessed within a program
#A variable is only accessible within the region where it is defined...
'''
Types of Scope :Local Scope,Global Scope,Global Keyword,Nonlocal Scope

#Local Scope:Variables defined and accessible only inside the function..

def fname():
    """Usage of local variables"""
    name = "Codegnan"
    return f'{name} is in Vizag'
print(fname())
#print(name) #NameError as LocalScope name is inside the function
print(fname())
name = "Saketh"
print(name)

#Global Variable -->A variable declared outside all functions is called a
#global variable.It can be accessed from anywhere in the program
name = "Codegnan"
def uname():
    """Global Scope"""
    return f'{name} is in Vizag,Vijayawada and Hyderabad.'
print(uname())
print(name)

#Local variables get higher priority inside the function
name = "Codegnan"
def uname():
    """Global Scope"""
    name="Saketh"
    return f'{name} is in Vizag,Vijayawada and Hyderabad.'
print(uname())
print(name)

#Global keyword --> Used when we want to modify a global variable
#inside the function
count = 15
def update():
    """Global Keyword usage"""
    global count
    count =count+5 #UnboundLocalError so we need to use global keyword
    return f'Updated count is {count}'
print(update())
print(f'New Count is {count}')
values =[1,3,45]
values.append(count)
print(values)

#NonLocal Scope -->Used in Nested Functions..Allows modifications of
#variables from the outer function

def outer():
    """Outer Function"""
    count=10
    def inner():
        """Inner Function"""
        nonlocal count
        count = count+15
        return f'Result from Inner function is {count}'
    print(inner())
    return f'Result from Outer function is {count}'
print(outer())

#LEGB   --> Local,Enclosing-->Global ---> Built-in

len = 45
a = ['codegnan','python']
#print(len(a)) #Here we have used built-in function as identifier it fails
'''
#Functions are termed as First class Objects
#Pass by Value and Pass by Object Reference


#Pass by Value --> Immutable objects
#int,float,bool,str,tuple,complex,frozenset
#When immutable objects are passed to function,changes inside the function
#donot effect the original value
#Original value remains unchanged
'''def update(number):
    """Pass by value usage"""
    number = 15
    print("Inside Function:",number)
number = 20
update(number)
print("Outside value is",number)
'''
def update(number):
    """Pass by value usage"""
    return number * 3
    print("Inside Function:",number)
number = 20
print(update(number))
print(update(25))















































































































































































    






















































































































































































