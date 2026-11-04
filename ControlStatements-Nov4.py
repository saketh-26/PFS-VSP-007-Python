
'''
Usage of for with conditional statements -->for with else
Normal Completion --> Loop is going through the entire sequence naturally.
else block will run
Interruption --> Jumping statements (break,continue)

#notifications = [0,0,0,0]
notifications = [0,0,1,1,0,0]
#0 --> Notification read
#1 --> Unread notification
#Notification Checker
for notification in notifications:
    #you need to map a condition
    if notification == 1:
        print("Unread Notification")
else:
    print("All Notifications are Caught up")
#print("All Notifications are Caught up")    

#Searching scenario same above program to be transformed -->
#if target is found

#break -->terminate the flow of the program..
notifications = [0,0,1,1,0,0]
#0 --> Notification read
#1 --> Unread notification
#Notification Checker
for notification in notifications:
    #you need to map a condition
    if notification == 1:
        print("Unread Notification")
        break #it exits early,the else block will be skipped
else:
    print("All Notifications are Caught up")
#print("All Notifications are Caught up")

#Searching in a List
#You want to handle the "item not found" case

fruits = ["apple","banana","kiwi","cherries"]
item = input("Which fruit u want:").lower()
for fruit in fruits:
    if item == fruit:
        print(f'You got your desired {item}')
        break
else:
    print(f'Could not find {item} in the fruits')
'''
#continue --> will skip the current iteration and proceeds for the
#rmng iteration
'''
fruits = ["apple","banana","kiwi","cherries"]
item = input("Which fruit u want:").lower()
for fruit in fruits:
    if item == fruit:
        print(f'You got your desired {item}')
        continue
else:
    print(f'Could not find {item} in the fruits')

#observe by modifying usage of break and continue with else blocks

notifications = list(map(int,input("Enter the values:").split(',')))
print(notifications)
for notification in notifications:
    #you need to map a condition
    if notification == 1:
        #pass   it is mainlyused as a placeholder
        print("Unread Notification")
        continue
        #break
else:
    print("All Notifications are Caught up")
'''
#while --> Loops -->it is mainly used when we rely condition,it will be
#completely executed until the condition is satisified

'''
while <condition>:
    statement(s)....
    ......

while True:
    print("Yes") #it runs an infinite loop we need to keyboard interrupt

#initalizer with which we need to initalise

i = 0 #initialised statement
while i<=10:
    print(i)
    i = i+1 #counter

#Get the counter from 10 to 1 using while
i = 10
while i>=1:
    print(i)
    i = i-1 #decrement
'''
i = 0
while i<=10:
    print(10-i)
    i = i+1 #counter



















    








    



    











    

































    


























































