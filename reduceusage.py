'''
reduce() --> It reduces an iterable into a single value..It
repeatedly applies a function to combine elements..

we can use it from functools
syntax --> reduce(function,iterable)
'''
import functools
from functools import reduce
'''
#Sum of numbers from a iterable
numbers = [1,5,2,3,4]
result = reduce(lambda a,b:a+b,numbers)
print(result)

#Largest Number from a collection
data = list(map(int,input().split()))
print(data)
result = reduce(lambda a,b:a if a>b else b,data)
print(result)

#Return the longest word in a group of strings

words = ['Python','Developer',"SQL","Programming"]
longest = reduce(lambda a,b : a if len(a) > len(b) else b,words)
print(f'Longest Word : {longest}')
'''
#list Comprehensions --> In Python,it is a precise way to create
#Lists
#Syntax ---> [expression for item in iterable]
#iterable --> list,set,dict or range()
'''
li = []
for i in range(10):
    #print(i)
    li.append(i)
print(li)

li = [i for i in range(10)]
print(li)

#Squares of 1-10 numbers in a list
squares = [i**2 for i in range(1,11)]
print(squares)

#get the even numbers in a list
even_numbers = [int(i%2== 0) for i in range(1,11)]
print(even_numbers)
even_numbers =[i for i in range(1,11) if i%2==0]
print(even_numbers)

#Update scores of each person with 10marks
scores = [25,45,50,60,55]
f_scores = [i+10 for i in scores]
print(f_scores)
m_scores = list(map(lambda i:i+10,scores))
print(m_scores)

names = ['saketh','codegnan','vizag']
#result = ['SAKETH','CODEGNAN','VIZAG']
result = [i.upper() for i in names]
print(result)
result = list(map(lambda i:i.upper(),names))
print(result)

#List Comprehension with if-else usage
#[true_value if condition else false_value for item in iterable]
data=[12,4,5,6,8,9]
result = ["Even" if i%2==0 else "Odd" for i in data]
print(result)
result = [i**2 if i%2==0 else i**3  for i in data]
print(result)

#nested List comprehensions --> One inside another
#[expression for i in iterable1 for j in iterable2]

colors =['Red','Blue','White']
sizes = ['S','M','L','XL']
dress = [(color,size)for color in colors for size in sizes]
print(dress)

d=[(i,j) for i in range(1,5) for j in range(1,5)]
print(d)
print(*d)

data = [i*j for i in range(1,6) for j in range(1,6)]
print(data)
#Multiplication table pattern
data = [i*j for i in range(1,11) for j in range(1,11)]
#print(data)

for table in data:
    print(table,end=" ")

print(*data)
#get the table pattern in vertical order

#Nested Comprehension with if condition
#Syntax:[expression for i in iterable1 for j in iterable2 if condition]
#possible pairs without matching values
data = [(i,j) for i in range(1,4) for j in range(1,4) if i!=j]
print(data)

f = [i*j for i in range(1,4) for j in range(1,4)if i!=j]
print(f)
print(*f)
'''
#nested Comprehension with if-else usage
#[true_value if condition else false_value
#for item1 in iterable1 for item2 in iterable2]

week_1 = [15,20,21,22,18,19]
week_2 = [23,19,25,18,19,25]

result = ["Improved" if x<y else "Lagged" for x in week_1 for y in week_2]
#print(result)
#make sure to check the braces and closures
#In the above case if we replace [] braces with () --> wedont get tuple

#Generators

#result = ("Improved" if x<y else "Lagged" for x in week_1 for y in week_2)
#print(result)

#Generator --> It is a Special Function,which produces one value at a time
#we use yield keyword
'''
def fname():
    """doc string"""
    return value(s)...
    ....
fname()

def fname():
    """Doc string"""
    yield value1
    yield value2
    yield value3
    ......
fname()
'''
'''
def func():
    """Normal Function"""
    return [1,2,3,4,5]
    #return "Saketh"    #A function can have return with multiple values
#print(func())
data = func()
for i in data:
    print(i)

def func():
    """Generator Function"""
    yield 1
    yield 2
    yield 3
#print(func())
b = func()
print(next(b))
print(next(b))
print(next(b))
#print(next(b)) It raises StopIteration as values are already fetched

def display():
    """Subjects Covered"""
    yield ["Python",45,'Paperbased Exams']
    yield ["Aptitude",65,'Weekly Exams']
    yield ["Softskills",60,"Activities"]
    yield ["Frontend",45,"Projects"]
    yield ["FASTAPI",45,"Integration"]
print(display())
g = display()
print(f'Subject alloted is {next(g)}')
print(f'Subject alloted is {next(g)}')
print(f'Subject alloted is {next(g)}')

week_1 = [20,14]
week_2=[15,20]
result = ("Improved" if x<y else "Lagged" for x in week_1 for y in week_2)
#print(result) #it returns a generator
g = result
print(next(g))
print(next(g)) #next() function will fetch the value from generator
print(*result) 
'''
#Exception Handling --> It is the mechanism in Python to respond to
#Runtime Errors or Exceptions
#Exception isan event that occurs during the execution of a program
#which disrupts its normal flow..

#TypeError,ValueError,IndexError,AttributeError,KeyError,ZeroDivisionError.

#We will be using try,except and finally..
'''
Syntax:
try:     #you write code which may cause an error
    #code that raise an exception 
except ExceptionType:   #it handles the error if it occurs
    #code to handle the exception

#Basic Exception handling
a,b = 5,0
try:
    result = a/b
    print(f'Answer is {result}')
except Exception as e:
    print(f'Error is {e}')

#a,b = map(int,input("Enter the values:").split())
#print(a,b)
try:
    a,b = map(int,input("Enter the values:").split())
    #print(a,b)
    result = a/b
    print(f'Answer is {result}')
except Exception as e:
    print(f'Error is {e}')

#Multiple Except Blocks
try:
    a,b = map(inter,input("Enter the values:").split())
    #print(a,b)
    result = a/b
    print(f'Answer is {result}')
except ValueError:
    print("Values should be only 2 and only integers")
except ZeroDivisionError:
    print("Cannot divide by zero")
except NameError:
    print("Sariga chusi rayuuu")

try:
    subjects=['Python',45,'AI',30]
    #print(subjects[5])
    subjects.apend("SQL")
    print(subjects)
except Exception as e: #this can be written if u want exception to take care
    print(e)
except IndexError:
    print("make sure to check the length")
except NameError:
    print("Check the spelling")
except AttributeError:
    print("Check the method properly")
finally:
    print("Anyways this will be printed....")

#Catching Multiple Exceptions Together
try:
    value = int(input("Enter a value:"))
    #result = 10/vlue check this case
    f = 10/value
    print(f)
except (ValueError,ZeroDivisionError,NameError) as e:
    print(f'An Error occured:{e}')
'''
#Raising Exceptions
#You can raise exceptions intentionally using raise keyword
'''
value = 15
if value < 0:
    raise ValueError("Value cannot be negative")
#else:
#    print("Done")

Custom Error Messages:
try:
    raise Exception("Custom Error Message")
except Exception as e:
    print(e)
'''
try:
    value = -15
    if value < 0 or value in [1,20]:
        raise Exception("Value is negative")
except Exception as e:
    print(e)

def fn(a,b):
    """testing"""
    return a**b
print(fn(10,3))

































































































































































    



























    
















































































































































































    


















































