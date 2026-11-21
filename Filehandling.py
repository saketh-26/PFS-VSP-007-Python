'''
File Handling --> open()

File and directory operations are essential to store the data..
Python provides build-in function--> open()
'''
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
