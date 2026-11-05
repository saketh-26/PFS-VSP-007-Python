'''
while --> initalized statement,counter...

#Banking Scenario -->PIN authentication if more than
#3 attempts Account locked

pin = "2612"
max_attempts = 3
#You need to have a current attempt
current_attempt = 0
while current_attempt < max_attempts:
    enter_pin = input("Enter the ATM pin")
    if enter_pin == pin:
        print("Login Successful")
        print("Withdraw the Money...")
        break
    else:
        print("Entered PIN is wrong.Try again carefully")
        current_attempt += 1
else:
    print("Account Locked...Try again after 24hours")


#BMI Scenario (Usecase),we will makeuse of Control Block Statements:

#BMI -->Body Mass Index --> bmi = weight(kgs) / (height**2) (metres)

Feet --> 1 feet -->12 inches --> 2.54cm --> 30.48cms
    -->5 feet 6 inches --> 167.78 cms --> 1.67 metres

n = int(input("How many users:"))
for i in range(n):
    weight = int(input("Enter the weight in kgs:"))
    height = float(input("Enter the height in metres:"))
    name = input("Enter the name:")
    if weight > 0 and height > 0:
        bmi = (weight) / ((height)**2)
        #print(bmi)
        #(<18.5 --> Underweight,18.5 - 24.9 --> healthy,25-29.9 --> Overweight
        #>=30 --> Obesity)
        if bmi < 18.5:
            print(f'{name} --> You are Underweight as BMI is {bmi}')
        elif bmi >=18.5  and bmi <=24.9:
            print(f'{name} --> You are in perfect physique,BMI is {bmi}')
        elif bmi >= 25 and bmi<=29.9:
            print(f'{name} --> You are Overweight need to maintain diet,BMI is{bmi}')
        elif bmi>=30:
            print(f'{name} -->Obesity,BMI is {bmi}')
    else:
        print(f'Enter only +ve values')

#Task : --> For same above BMI calculator,store the details in dictionary

#BMI_results = {'names':[user1,user2,user3.....],
#               'BMI_values':[bmi1,bmi2...]
O/p format:
BMI_results = {'names':['Akash','Vinay','Sandeep'],
               'BMI_values':[24.657,25.456,28.945]}
'''

#assert --> It is mainly used in debugging checking during development
#it tests whether a given condition is satisfied or not its
#a mandatory else it will raise the error.It is mainly used to catch bugs
#by ensuring the conditions hold True..

#Syntax:   assert <condition>,"Error Message"

x = int(input("Enter the value:"))
#assert x>0
assert x>0,"Enter only Positive value"
x = x**2
print(f'Final result is {x}')
assert x in [24,25,12,10],"Checking data"
print(f'Search Found')

































































        

 












































