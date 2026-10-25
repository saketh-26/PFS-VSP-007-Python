'''
Sequences -> Strings,Lists[],Tuples (), Sets set(),Dictionaries {}
Lists [] --> A list is an Ordered,Mutable,Indexed and heterogenous Collection
It will be dynamic in size,allow duplicates

#Creation of Lists
details = [123,"Saketh",32,"PFS",75.5]
print(type(details))
print(len(details))
print(details)

#Nested Lists
batches = [["PFS","PFS-VSP-007","PFS-VSP-008"],
           ["DA","DA-VSP-007","DA-VSP-008"],
           "Vizag",8]
print(len(batches))
print(type(batches))

#Indexing,Slicing,Striding
print(batches[0])
print(batches[-3])

print(batches[1:4]) #observe the output
print(batches[:2])
print(batches[1:5:2])

print(batches[-5:-1:4])
print(batches[-1:-5])

#Subindexing -->Accessing index within the index of a collection(str,list,tuple)

print(batches[0])
print(batches[0][1])
print(type(batches[0][1]))
print(batches[0][1][4:7])
print(batches[0][1][4:7][::2])

#Lists supports Repetition,Merging and its also an Iterable (iterate through
#loops)

print(batches[0][1])
print(len(batches[0][1]))
print(batches[0][1][:3] + batches[0][1][-4:])

print([1,2,3] *3) #repetition
#print([1,2,3]+3) #TypeError
print([1,2,3] + batches)#Merging
a = [1,2,3]
b = a*3
print(len(b))

print(batches)
print('Vizag' in batches) #Membership 
print('PFS' in batches)
print('PFS' in batches[0]) #returns True

#lists methods
data = []
#print(dir(data)) #returns list of all available methods
#append(),extend(),insert()
#append(obj) --> insert objct to the end of the list
data.append(24)
print(data)
data.append('vizag')
print(data)
#data.append('Python','MYSQL') #TypeError 
data.append(["Python","MYSQL"])
print(data)
print(len(data))
#append() will always increment the length by 1
#extend()-->insert multiple elements (objects) to the end of the list
print(data.extend(['Python','MYSQL']))
print(data) #in this case list length becomes 5 as we have inserted
#two objects from the iterable
data.extend('vizag') #check this 
print(data)
#insert(index,object) -->inserts elements before index

data.insert(2,'saketh')
print(data) 

data.insert(-3,'codegnan')
print(data)

data.insert(2,[34,45,6])
print(data)

#Lists are mutable
marks = [25,24,27,28,30,35,36]
print(marks)
marks[2] = 45
print(marks)
marks[:3] = ['saketh','codegnan']
print(marks)
#In above cases data is being modified in original list
#(Indexing case length remains constant but data is modified,
#whereas in slicing case it may increase,decrease)

#pop(),remove(),clear() ->removes elements from the list
subjects = ['Python','Aptitude','SS','MYSQL','Flask']

#pop() --> removes by default last element if index is not mentioned
#print(subjects.pop()) #removes and returns last element
#print(subjects.pop(2))
#print(subjects.pop(5)) #raises IndexError
#print(subjects)
#remove() -->removes specific value from the collection (only first occurance)
subjects.remove("Python")
#print(subjects.remove("Python")) #returns None 
#subjects.remove("Codegnan") #ValueError
#clear() -->removes all elements from the list and returns empty list

subjects.clear()
print(subjects)

#index(),count()
#index(start) #returns only first occurance index postion
marks = [24,25,24,26,27,30]
print(marks.index(24))
print(marks.index(24,1)) #here we are exclusively giving start postn
#print(marks.index(545)) #ValueError

#count() -> returns the count of occurances
print(marks.count(24))
print(marks.count(248))

#Task:Create a Nested List with lists and strings and perform List methods

#copy(),sort(),reverse()

details = [['Sanjay','Python',50],
           ['Akash','Flask',45],
           ['Vinay','Aptitude',30]]
#print(details)
#print(len(details))

#copy() -->creates a shallow copy of the given collection
data = details.copy()
#print(data)
#print(len(data))

data[0].append("A") #Nested list changes will be directly applicable
#in both lists
data.append("Vizag")
print(data)
print(len(data))
print(details)
print(len(details))

data.extend(["PFS","JFS"])
print(data)
print(len(data))
#print(details)
#print(len(details))

details.extend(["Hyd","Vizag","Vijayawada","Codegnan"])
print(len(details))
print(len(data))

#In the below case we have created basic lists so original is not effected
subjects = ['Python','MYSQL','Aptitude','Softskills']
#data = subjects.copy()
#print(data)

#data.insert(2,"Frontend")
#print(data)
#print(subjects)

data = subjects  #this is like complete clone of original data
data.insert(2,"Frontend")
print(data)
print(subjects)
subjects.remove("Python")
print(subjects)
print(data)
'''
#sort() reverse()

marks = [12,15,20,24,21]
#print(marks.sort()) #returns None as nothing to be returned
#print(marks)

#marks.sort(reverse=True) #it returns in descending order
#print(marks)

#marks.append("Saketh")
#marks.sort() #raises TypeError
'''
marks.extend([-23,12,87])
print(marks)

marks.sort(reverse=True) #descending order
print(marks)

print(marks)
#marks.reverse() #returns in reverseorder
#print(marks)
marks.extend(['poll','sunday',123])
marks.reverse() #this will make changes in original list
print(marks)
print(marks[::-1]) #this will just return the reverse order as o/p

#min(),max(),len(),type(),sorted()
marks = [20,12,23,25,30]
print(marks)
print(min(marks))
print(max(marks))
b = sorted(marks) #sorted() function returns a new list with elements in
#ascending order
print(b)
print(marks)


#Tuples -->Tuples are Immutable,Ordered,Indexed Collection,it can also have
#duplicates,we use () to store the data..

data = ()
print(type(data))
print(len(data))

data=1,2,3,4, #by default it stores in tuple
print(data)
print(type(data))

#be very specific when we are passing data using ()
#Tuples are Immutable we cannot modify the elements in it
#data[-2] = 'codegnan' #it is not possible
#Nested Tuples (also will have lists in it)
'''

details = ("Vizag",8,("PFS","JFS","DA"),["Aptitude","Softskills"])
'''print(len(details))
print(details[:2])
print(details[2][1]) #subindexing
print(details[2][::2])

print(details[-1])
details[-1].extend(['Python','Java'])
print(details)

#we cannot make any changes over tuple directly but we can change on list
print(details[0].upper())
print(details)

#Indexing,Slicing,Repetition,Merging are possible

temp = (23.5,24,34.5)
b= temp*2
print(b)
print(b + temp)

#Tuple Methods --> index(),count()
data = (12,3,24,3,12,4,5)
print(data)
print(data.index(3))
print(data.index(3,2))
print(data.count(3))

b = sorted(data) #returns sorted elements in a list
print(tuple(b))
c = tuple(sorted(data,reverse=True)) #returns tuple in descending order
print(c)

del data #it completely eliminates the variable
#print(data) #NameError
'''

#Sets : A Set is an Unordered,Unique,Mutable collection.It will never
#allow duplicates

ids = set()
print(ids)
print(type(ids))

names = {'saketh','raju',24,3,'raju',24}
print(names)
print(len(names))

#d = {12,3,4,[12,3,4],45} #We cannot have lists inside a set
#print(d)

d = {12,3,4,(12,3,4),45} #we can have tuples in a set
print(d)

#Task : Create a Nested Tuple with lists inside it and make all methods
#of lists in the Tuple.






























































































































































































































































































































