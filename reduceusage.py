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
'''
#nested List comprehensions --> One inside another
#[expression for i in iterable1 for j in iterable2]

colors =['Red','Blue','White']
sizes = ['S','M','L','XL']
dress = [(color,size)for color in colors for size in sizes]
print(dress)

d=[(i,j) for i in range(1,5) for j in range(1,5)]
print(d)
print(*d)








































































    


















































