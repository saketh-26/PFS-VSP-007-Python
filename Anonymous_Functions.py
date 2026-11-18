'''
Functions are termed as First Class Objects...

Anonymous Functions : An Anonymous Function is a nameless function,we use
lambda keyword to use it..

They are generally used for short simple,operations can be written
in a single line,they are also termed as Lambda Functions..They are
generally used with filter(),map() and reduce()

Syntax : lambda argument(s) : expression

#Create a function to get the area of rectangle
def rectangle(l,b):
    """Area of Rectangle"""
    return l*b
print(rectangle(7,5))


area = lambda l,b : l*b
print(f'Area of Rectangle is {area(7,5)}')

#Square of a number --> Normal Function -->Lambda Function

def square(number):
    """Square of a number"""
    return number ** 2
number = int(input())
print(f'Square of {number} is {square(number)}')


number = int(input())
sqaure = lambda number : number **2
print(f'Square of {number} is {square(number)}')

#Find Maximum of two numbers

def maximum(a,b):
    """Maximum logic"""
    return a if a> b else b
print(maximum(10,35))

maximum =  lambda a,b : a if a> b else b
print(maximum(10,35))

#No Parameters
greet = lambda :"Welcome to Vizag"
print(greet())


#filter() used to select elements from an iterable based on a condition
#Only the elements that satisfy the condition are returned

#filter(function,iterable)

numbers = [1,2,4,6,7,8,9,10,12,45,67]
#Even numbers  --> [2,4,6,8,10,12]
#Normal Function

def even(numbers):
    """Even Numbers from list"""
    even_list = []
    for num in numbers:
        if num%2 == 0:
            even_list.append(num)
    return even_list
print(even(numbers))

result = list(filter(lambda num:num%2==0,numbers))
print(result)

odd_result = list(filter(lambda num:num%2!=0,numbers))
print(odd_result)

prices = [500,650,1200,800,900]
#Products above 700
result = list(filter(lambda price:price>700,prices))
print(result)

#map() applies transformation to every element in a collection
#map(function,*iterables)

scores = [15,20,19,23]
result = list(map(lambda new_score:new_score+1,scores))
print(result)

d= list(map(int,input().split())) #list of integers
print(d)
'''
#Add GST -->18%
prices = [1000,5000,4500]
final_price = list(map(lambda price:price + (price*0.18),prices))
print(final_price)

#Cal length of objects in a collection
subjects = ['Python','SQL','Aptitude','Softskills']
result = list(map(lambda word:len(word),subjects))
print(result)
















































































       














































































































