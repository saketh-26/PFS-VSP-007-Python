'''
Tokens,Datatypes (Numeric,Boolean,NoneType,Sequences (str,lists,tuples,sets,
frozensets,mapping objects (dicts)) Typecasting
Operators
Input Formatting / Output Formatting

#Input Formatting --> input()

#Usage of input()
#We can pass any type of object as input --> result is in only string

name = input("Enter the name:")
print(name)
print(type(name))

#Integer Input --> int() --> if u mismatch value --> ValueError
roll_number = int(input("Enter the Roll Number:"))
print(roll_number)
print(type(roll_number))

#Float Input --> float()-->we can pass either integer / decimal value --> float
marks = float(input("Enter the Marks:"))
print(marks)
print(type(marks))

#Group of strings (Group of values as strings)
#Space separated values --> we need to give one space after each object
#returns List
names = input().split() #no need of prompt (Competitive Coding Platforms)
names = input("Enter the names:").split()
print(names)
print(type(names))

#Comma Separated Values
subjects = input("Enter the Subjects:").split(',')
print(subjects)
print(type(subjects))

#Multiple values (more than one)inputs --> result is always string
#make sure to match the arguments
name,batch = input("Enter the details:").split()
print(name)
print(batch)

#Multiple integer values 
#we will use map()
order_id,cost = map(int,input().split())
print(order_id)
print(cost)

#We want to take subjects marks
py_marks,ap_marks,ss_marks,sql_marks = map(float,input().split())
print(py_marks,ap_marks,ss_marks,sql_marks)

#Group of Integers,float values
#List of Integers
stu_marks = list(map(int,input("Enter the marks:").split(',')))
print(stu_marks)
#Float of Integers
discounts = list(map(float,input("Enter the discounts:").split(',')))
print(discounts)

#Accept the cost of selling the product from user and also the original cost
#of the product and determine the profit / loss amount for the user

original_amount = float(input("Enter the Original Cost:"))
selling_amount = float(input("Enter the Selling Cost:"))
orignal_amount,selling_amount = map(float,input().split())
profit = selling_amount - original_amount
print(profit)

#Set of Integers
#Set of Float values -->replace int with float
ids = set(map(int,input("Enter the IDS:").split(',')))
print(ids)
print(type(ids))

#Passing list() as input using eval()
#u can directly pass same as list,tuple,set data as it is
list_data = eval(input("Enter the list values"))
print(list_data)
print(len(list_data))
tuple_data = eval(input("Enter the tuple values"))
print(tuple_data)
print(len(tuple_data))
set_data = eval(input("Enter the set values"))
print(set_data)
print(len(set_data))
#passing dict data using eval

stu_details = eval(input("Enter the data:"))
print(stu_details)

#So using eval() u can pass any type of data

#Output Formatting --> print()
a,b,c = map(str,input("Enter the names:").split())
print(a,b,c)
#now we will use sep --> sep is the keyword
print(a,b,c,sep="----")
#end is specifically telling how u wanna end the statements
print(a,b,c,sep=":",end='\t') #here end = tab space character
print("Saketh","Vizag",end=" ") #here end = space character
print(34,4.5)

#1) Using commas in print() -->we separate by commas
name = "Codegnan";branch = "Vizag";batch = 'PFS-VSP-007'
print(name,"is in",branch)
print(batch,"belongs to",branch,"branch")

#2) Using %(modulus) formatting -->Old Style C Programming
#%d -->integers,%f -->float,%s -->strings
age = 32
price = 45.256
place = "Vizag"
print("Age = %d | Price = %f | Place = %s"%(age,price,place))
print("Price is %.f"%price) #in this case complete decimal part is wiped off
print("Price is %.2f"%price) #rounding off to two decimals
'''

#3) Usage of String formatting --> str.format()

name = "Codegnan";branch = "Vizag";age = 8
print("{} is in {} and its of {} years in Edtech Industry".format(name,
                                                                 branch,
                                                                  age))
a,b = 2,45
print("{1},{0}".format(a,b))
print("Value of a is {} and value of b is {}".format(a,b))

#f-string notation --> Python 3.9+ versions
print(f'{name} is in {branch}')
#make sure to denote the variables only in curly braces
print(f'Value of a is {a} and b is {b}')
print(f'"Codegnan is in {branch} and of {age} years in Trainings"')





































