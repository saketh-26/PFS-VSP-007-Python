'''
Datatypes --> It will tell us how to define the data
Numeric Datatypes -->integer,float,complex
Boolean type --> True/False
None type -->None
Sequence types -->strings,lists,sets,frozensets,mappings(dictionaries)
'''
#Python by default follows Implicit type
#Numeric datatypes -> integer -->quantities,ids,order ids,stock,age -->int
'''age = 32
print(age)
print(type(age))
stock = 35
print(type(stock))
batch_rank = 1
print(batch_rank)

#float values -->salaries,price,percentage calculations,temp.... -->float
salary = 15125.45
print(salary)
print(type(salary))
temp = 34.5
print(type(temp))

#complex --> real and imaginary values -->scientific calcns,signal processing
#i5 = 23
#data = 3+i5 #in this case addition will be done
#print(data)

data = 3+5j
print(data)
print(type(data))

#Boolean -->True/False -->validations
access = True
print(type(access))
result = False
print(type(result))

#Nonetype --> None
##None --> 0,False,'',[],(),{},set() --> None cases in Python
branch_rank = None
print(type(branch_rank))

#TypeConversion ->converting one datatype to another datatype
#explicit conversion 

#integer -->float,complex,boolean
#Every built-in datatype is a built-in function
rank = 5
print(type(rank))
b = float(rank)
print(b)
print(type(b))
c = complex(rank)
print(c)
d = bool(rank) #bool(anything) is True,bool(nothing) -->False
print(d)
print(type(d))
#Space is also a character
print(bool([''])) #empty string inside a list
#float --> integer,complex,boolean

price = 45.25
print(type(price))
a = int(price)
print(a)
b = complex(price)
print(b)
c = bool(price)
print(c)

#complex --> int,float,bool

signal = 5+6j
#c = int(signal) #raises TypeError (invalid datatype)
#print(c)
#d = float(signal)
e = bool(signal)
print(e)

#boolean --> int,float,complex

access = True
print(int(access))
print(float(access))
print(complex(access))
print(bool(access))

a = int(float(bool(5)))
print(a)
b = bool(float(int(34))) #check for the outer one
print(b)

c = True + 35 + 3.5 + (6+5j) #True becomes 1
print(c)

#Sequence types --> strings,lists,sets,frozensets,dictionaries
#Strings --> Group of characters
#quotations -->single,double,triple quotes
place = "codegnan"
print(type(place))
name = 'Saketh'
print(name)
#Strings are Immutable,Ordered,Indexed collection
print(len(name)) #len(obj) -->returns the number of items in a collection
print(len(place))
print(len('qwerty'))

#Space is also a character
a = " "
print(a)
print(len(a))
'''
#Converting strng -->int,float,complex,boolean
course = 'Python'
#print(int(course)) #ValueError
#print(float(course)) #raises ValueError
#print(complex(course))
print(bool(course))

#int -->str
#float -->str
#complex -->str
#bool -->str

data= 56
b = str(data) #it becomes numeric string
print(b)
mileage = 13.5
c = str(mileage)
print(type(c))
d = str(3+5j)
print(d)
e = str(True)
print(e)







































