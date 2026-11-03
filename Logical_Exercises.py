'''
Best Seller Tag Display
Write a Python program to display "Best Seller" if the
product sales are greater than 1000.
Test Case 1
Input:
1200
Output:
Best Seller
Test Case 2
Input:
800
Output:
No Output

n = int(input("Enter the sales"))
if n > 1000:
    print("Best Seller")
else:
    print("No Output")

Zepto Rain Delivery Charges
Zepto applies additional delivery charges during rainy weather due to increased delivery
difficulty. Write a Python program that checks whether it is raining and displays "Extra Rain
Charges Applied" if the condition is True. Use an if statement only.
Test Case 1
Input:
True
Output:
Extra Rain Charges Applied
Test Case 2
Input:
False
Output:
No Output

raining = bool(input())
print(raining)
print(type(raining))
if raining:
    print("Extra Rain Charges Applied")
else:
    print("No Output") #we will get this when we dont pass any input

Delivery Charge Calculation :

A food delivery app offers free delivery for orders above ₹99. If the order value is ₹99 or
below, a delivery charge of ₹30 is added to the bill. Write a Python program to calculate and
display the final bill amount using an if-else statement.
Test Case 1
Input:
150
Output:
Final Bill Amount: 150
Test Case 2
Input:
80
Output:
Final Bill Amount: 110

order_value = int(input("Enter the Order Value:"))
if order_value > 99:
    print(f'Final Bill Amount:{order_value}')
else:
    print(f'Final Bill Amount:{order_value + 30}')

Weekend Planner Based on Budget
Write a Python program to suggest a weekend plan based on the user's budget.
Conditions:
Budget > 10000 → Trip
Budget > 5000 → Resort Stay
Budget > 3000 → Movie and Dinner
Budget > 1000 → Cafe and Shopping
Budget > 500 → Street Food and Park Visit
Otherwise → Stay Home
Test Case 1
Input:
12000
Output:
Plan: Trip
Test Case 2
Input:
5000
Output:
Plan: Movie and Dinner
Test Case 3
Input:
100
Output:
Plan: Stay Home

budget = int(input("Enter the Budget:"))
if budget > 10000:
    print("Plan: Trip")
elif budget > 5000:
    print("Plan: Resort Stay")
elif budget > 3000:
    print("Plan: Movie and Dinner")
elif budget > 1000:
    print("Plan: Cafe and Shopping")
elif budget > 500:
    print("Plan: Street Food and Park Visit")
else:
    print("Plan: Stay Home")
'''

#Repetition Statements (Loops) --> Loops helps us in automating repetitive
#tasks--> for,while
#Usage of for: -->It is used mainly to iterate within in lists,strings,
#ranges..
'''
Syntax :
for <temp> in collection/range:
    statement(s)...
    .......
    ......

#marks = [25,20,21,19,10,12]
#Marks can be dynamic
marks = list(map(int,input("Enter the marks:").split(',')))
for i in marks:
    print(i) #it traverses within the loop
#Cal the total marks

marks = list(map(int,input("Enter the marks:").split(',')))
total = 0
for mark in marks:
    #print(i) #it traverses within the loop
    #we need to update total with each mark
    total = mark + total    #total += mark
    print(total)
print(f'Total marks are:{total}')
print(f'Avg marks are :{total/len(marks)}')

subject = input("Enter the subject:")
for i in subject:
    print(i)

details = {'ids':[121,123,125],
        'marks' : [25,20,21]}
for data in details: #indexed through keys
    #print(data)
    print(details[data]) #it returns values

for data in details.values():
    print(data)
for key,value in details.items():
    print(key,value)

#range(stop) --> takes by default minimum value as 0
for i in range(5):
    print(f'Value of i is {i}')
    print(f'Square of i is {i**2}')

#range(start,stop) -->u can mention start and stop postns(values)
#start is included,end is excluded
for i in range(1,11):
    print(i,i**2)
    print('<----->')

#range(start,stop,step)
for i in range(1,21,1):
    print(i)
for i in range(1,21,2):
    print(i)

#Get first 10 even numbers
#print numbers from 10 to 1 in reverse order
for i in range(10,0,-1):
    print(i,end=' ')

#print 'A' to 'Z' in a single line
for i in range(65,91):
    #print(i,chr(i))
    print(chr(i),end=' ')
'''
names = ['Akash','Kaushik','Vijay','Sanjay','Lokesh']
for name in names:
    print(name,end=' ') #this returns in horizontal order

for i in range(len(names)):
    print(names[i]) #names[0] -->Akash -->names[1] -->kaushik

#Ask integer input from user and get the sum of numbersas per input
'''
Test-1:
4
10

Test-2:
6
21


Test-3
-5
No Output

n = int(input("Enter a value:"))
if n>=0:
    result = 0 #target
    for i in range(n+1):
        #print(i)
        result = result + i
    print(f'Result of {i} is {result}')
else:
    print("No Output")
'''

#Usecase : Checking daily workout app usage
work_log = [1,1,1,0,1,1,0]
#1 -->workout done
#0 --> workout missing
#Find the longest workout streak
longest_streak = 0#target
current_streak = 0
for day in work_log:
    #print(day)
    if day == 1:
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0
print(f'Longest Streak is {longest_streak}')
        


































































    























    
    


























































































    



























    





















    



