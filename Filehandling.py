'''
File Handling --> open()

File and directory operations are essential to store the data..
Python provides build-in function--> open()

#mode of operations --> 'r','w','r+','w+'
#open(filename,mode) #default mode is 'r'
try:
    file = open('new.txt',"r")
    print(file)
    #print(file.read()) #reads the entire content
    #print(file.readline()) #reads a single line
    print(file.readlines()) #read all lines into a list
except Exception as e:
    print(e)

f= open('new.txt')
print(f.read())
f.close()

#Best practice is we will use with statement
with open('new.txt','r')as file:
    print(file)
    print(file.read())

#Writing to a File
#'w' mode will create a new file if not existing,else if already exists
#it will override the content
g = open('new.txt','w')
print(g)
g.write("Saketh")
g.close()

h = open("today.txt","w")
h.write("PFS-VSP-007 is good but sometimes mischevious")
h.write("\n They make it as gang")
logs =['\nFirst ID','\nVinay','\tAjay']
#h.write(logs) #it needs only text
h.writelines(logs) #writelines(iterable) --> writes an iterable of
#strings(such as list or tuple)
h.close()
print("Done")

subjects = ['Python','\nSQL','\n Aptitude']
with open("qwerty.txt","w") as file:
    file.writelines(subjects)
    #print(file.read()) #IO Error

#when we use with block,we need not use close()

#Appending to a file -> if file is already existing no change u can add the
#content,if not new file will be created
with open('today.txt','a') as file:
    file.write("\n Students need to finish last week AI Mock Interview")
    file.writelines(["\n Vijay","\t Kaushik","\t Vinay",
                     "\n always chatting"])
    #print(file.read())

#usecase: Logging System
def log_activity(activity):
    """User Logs to be stored"""
    try:
        with open('log.txt','a') as log_file:
            log_file.write(activity+'\n')
            log_file.read() #it will get into except block
    except Exception as e:
        print("Error is",e)
    finally:
        print("File Handling is important")
log_activity("Vinay Logged in for AI Mock Interview....")
log_activity("Vinay is testing his Microphone and Camera")
log_activity("Vinay started his AI Mock Interview")
log_activity("Vinay is writing  the code")
log_activity("Vinay has finished and report created")
'''
#r+ --> read and write -->Preserves the exisitng content(data),
#new writes overwrite the characters from the start of the cursor..
'''
with open('saketh.txt','r+') as file:
    file.write("Testing phase")
    print(file.read())

with open('log.txt','r+') as log_file:
    print(log_file.read())
    log_file.write("End of class")
'''  
#Now we will prform write first then read later
    
with open('log.txt','r+') as log_file:
    log_file.write("PFS-VSP-007")
    print(log_file.read())
#in above case we are performimg write frst content is overwritten
#from the start of the cursor and when u read it rmng content will
#be shown
#Use case: Modifyng or Updating parts of an exisitng file 







    






















    


































































    



















    























    

































