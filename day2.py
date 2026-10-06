"""
Python --> Opensource,High Level,Interpreted,Scripting,POP,OOP,General
Purpose Language
Tokens -->Keywords,Variables,Literals,Operators,Punctuators,Identifiers

Tokens --> These are the smallest units in a program
Syntax -->how to write the script (program)

Keywords -->These are the reserved words in Python which has specific usage

35 keywords -->Condtional,loops,functions,classes,operators.....

#Variables -->Variables are named memory location that stores the data/
#it also acts as a placeholder.It also has some rules,It cannot start with
#a number,or a special character and no spaces in between,and no keyword usage

name = "Codegnan"
age = 8
place = "Vizag"
#print(names) #it raises NameError
#print(Age)
#Python is Case-Sensitive
email_id = "saketh@codegnan.com" #snakecase Convention (multiple words)
print(email_id)
branch_1 = "vijayawada" #we can use number anywhere but not at the start
print(branch_1)

#True = 45 #as True is a keyword we cannot use as avariable
#Comments --> It will make users understand what it it conveying
#Single Line Comment --> #
#Multi Line Comments  --> we can use triple quotes (Doc String)

#Multiassignment of variables #make sure to pass same number of values
name,email_id,mobile,gender = "Saketh","saketh@codegnan.com",8106429771,"Male"
#print(name,mobile)
#Python by default follows Implicit type (user need not allow)

#So u can prefer single line or multiple lines for assigning variables

name = "Codegnan";age=8;place = "Vizag"
print(name,age)

#Deletion  --> del 
del age #permanent deletion
del name,place
print(age)

#Swapping of variables
a,b = 15,25
print(a)
print(b)
a,b = b,a #value of a will become b
print(a)
print(b)

c = a #reassigning the exisiting value to a new variable
print(c)
#Literals -->These are constants/values such as numbers (int,float,complex)
#"hello" "good"
age = 32
print(age)
taste = "bad"
print(taste)
price = 115.45
print(price)
print(type(price)) #it returns the type of object
#type() is very very imp
print(type(age))
"""

#Identifiers --> names given to variables,functions,classes,objects,modules

#Punctuators --> [] --> Lists,()-->Tuples,{} -->Dictionaries,Sets
#Operators -->There are different type of operators --> Operations
#+,-,*,**,/ (Arithmetic Operators),//,% 
a = 5
b = 3
print(a/b) #/ --> Float Division (answer is always in float value)
print(a//b)  #Flooring Division (Integer division) returns quotient
print(a%b) #Modulus -->returns remainder

#Raju purchased Shoes with price 1000,discount 15%,
#now how much Raju has to pay?

price = 1000
discount = 0.15
final_price = price - (price * discount)
print(final_price)


#Vijay went to hotel for dinner his bill is 2500,GST applicable is 5%
#hotel manager has given him 5% discount,how much Vijay has to pay?











































