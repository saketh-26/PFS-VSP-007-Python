'''
String Methods --> Case Conversions,Replacing,Finding,White Trailing Spaces,
testing methods,alignment methods
'''
#Case Conversions --> upper(),lower(),title(),capitalize(),swapcase()
'''data = "Codegnan"
print(type(data))
#print(dir(data)) #dir() returns the available methods/functions
#upper() --> converts object to uppercase
print(data.upper())
e = data.upper()
print(e)
#lower() --> converts object to lowercase
f = data.lower()
print(f)
#capitalize() --> it will capitalize the first letter in the word
print("codegnan vizag".capitalize())
#title() --> it will capitalize every first letter in each word
print("codegnan vizag".title())

print("coDEgnan".swapcase()) #converts uppercase to lower and lower to upper

#Testing methods (which will give the result as Boolean (True/False)
#isupper(),islower(),isalnum(),isdigit(),isalpha(),startswith(),endswith()....

print("Codegnan".isupper())
print("codegnan".islower())
print("admin123".isalpha()) #returns True only when we have all alphabets
print("admin123".isalnum()) #returns True for an alphanumeric string
print("81234".isdigit()) #it checks for a digit string
print("Python".istitle()) #returns True
print("Python aptitude".istitle()) #returns False
print("Python".startswith('P'))

data = "Python Aptitude"
print(data.startswith("A"))
print(data[7:].startswith("A"))
print(data.startswith("A",7))
print(data.endswith("e"))
print(data.endswith("n",0,6))

print("12.34".isalnum())
print("12.34".isdigit())
print("½".isnumeric()) #fractions,roman numericals
print("XII".isnumeric()) #Roman numericas but we need to encode the data and
#get it

#Finding and Searching methods --> find(),index(),count()

data = "Codegnan is in Vizag"
print(data.find('a')) #returns only the first occurance
print(data.find('a',7)) #here we will check for the next occurances
#find() will return -1 if the given object is not present
print(data.rfind("a")) #rfind() will return the last occurance
#index(),rindex()
print(data.index("a")) #returns the first occurance
#if given object is not present it raises ValueError
#print("qwerty".index("s")) #raises ValueError
print("qwerty".index("werty")) #as substring is starting with 'w'
#rindex() returns last occurance
print("qwertywerty".rindex("y"))
#count() will return total number of occurances
print("Codegnan".count("n"))
print("Codegnan".count("t")) #returns 0 as 't' is not present

#split(),join(),strip(),lstrip(),rstrip(),zfill()
#split() returns the list of substrings from the string using separator
a = "Python Aptitude Softskills MYSQL"
b = a.split() #by default space is treated
print(b)
a = "Python,Aptitude,Softskills.MYSQL"
c = a.split(',')
print(c)
#join()
print("code".join("gnan")) #concatenates every object with the given iterable
print("#".join("Codegnan"))
print(" ".join("saketh"))

#White Space & Trimming methods -->strip(),lstrip(),rstrip()
a = "Saketh "
print(len(a))
a = a.strip() #removes leading and trailing whitespaces
print(len(a))

#Alignment Methods -->zfill() (make sure to pass the width >len(obj) it
#pads zero from left)
print("Python".zfill(10))
print("Codegnan".zfill(1))
print("Python".center(10,'*'))
print("Python".ljust(10,"*")) #returns the leftjustified string with fillchars
print("Python".rjust(10,"*")) #returns the rightjustified string with fillchars
'''
#Sequences --> Lists[],Tuples(),Sets set(),Frozensets,Dicts {}










































































