'''
Sequences --> Strings,Lists,Tuples,Sets,FrozenSets,Dicts

Strings --> A String is a group of characters,It is an immutable,Ordered,Indexed
Collection.We can denote it in single,double or triple quotes..

data = '' #empty string
print(type(data))
print(len(data))

#Operations --> Concatenation,Repetition,Indexed,Slicing,Membership
#Concatenation --> combining multiple strings
sub1 = "Python"
sub2 = "MYSQL"
print(sub1+sub2)
#output should be Python,MYSQL
#Python <-> MYSQL
print(f'{sub1},{sub2}')
print(sub1+" <-> "+ sub2)

#Repetition --> String can be repeated any number of items with avalid int
print("*")
print('*' * 10)
name = "Saketh";place = "Vizag"
print(f'{name * 10}*')
print(f'---->{name} is in ---->{place}')

#Membership --> in,not in
print("jay" in "Ajay")
print("Jay" in "Ajay") #returns False
'''

#Indexing -->Accessing each position(index) in an object
#It starts at 0 and ends at len(obj) - 1

name = "Codegnan"
'''print(name)
print(len(name))
#Traversing the elements --> Positive Indexing
print(name[2])
print(name[7])
#print(name[21])
#Negative Indexing --> starts from back it is denoted as -1 to len(obj)
print(name[-1])
print(name[-4])
#print(name[-9]) #IndexError
'''
#Slicing --> group of characters --> [start:end] start is included,end is
#excluded (len(obj) - 1)
'''print(name[:]) #returns all characters
print(name[0:])
print(name[0:4])
print(name[:4])
print(name[4:24]) #returns till end of string
print(name[24:]) #returns empty
print(name[5:1]) #returns empty string as positive slicing lower index to
#higher index

#name[2] = "saketh" #Strings are immutable


print(name)
print(name[-1:]) #returns only last character
print(name[-5:-1]) #same including negative indices with same symbols lower
#to higher index
print(name[:-6])
print(name[:-6]+name[-6:])
print(name[-1:-4]) #returs empty string

print(name)
print(name[1:-1])
print(name[-1:3]) #returns empty

#Task --> Create a string and explore above possibilties

#Striding --> [start:end:step] --> Now we can specifically get desired characters
#in an interval
print(name)
#print(name[::0]) #returns ValueError
print(name[::1]) #returns complete strng
print(name[::2]) #skips each alternate element from beginning
print(name[::3])

place = "Visakhapatnam"
print(place[:4])
print(place[7:])
print(place[-6:])
print(place[1:7:2])#first perform [1:7] then skip one element in it
print(place[2:18:5]) 
#what if we give -1 in interval
print(place[::-1]) #this helps to return in reverse order
print(place[::-2]) #this skips one element in reverse order
#You can explore all cases in Striding
print(place[1:9:-2])
print(place[-9:-1:1])
'''

#Built-in functions --> type(),len(),min(),max(),ord(),chr(),sorted()

password = "admin123"
print(len(password))
print(type(password))
print(min(password)) #min() returns min object in collection
#ASCII values follows
print(ord('A'))
print(ord('a'))
print(ord('z'))
print(chr(120))
print(sorted(password))





























































































































