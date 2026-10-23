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
'''

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

















































































