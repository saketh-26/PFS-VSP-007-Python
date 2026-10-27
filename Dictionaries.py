'''
Dictionaries -->A Dictionary is a Mutable collection,data is indexed
using keys,keys must be unique.Dictionaries Methods
'''
details = {'ids':['CGVI0242','CGVI0249',
                  'CGVI0224','CGVI0240'],
           'names':['Nikitha','Deepthi',
                    'Vinay','Tej'],
           'batch':'PFS-VSP-007',
           'place':('Vizag','Vjwda','Hyd','Bnglre'),
           'subjects':{'Python','Aptitude','Softskills'}}
#print(len(details))
#Membership
'''print('ids' in details)
print('Vinay' in details['names']) #we are accessing via keys
print('Python' in details['subjects'])

#print(details*2) #TypeError
#print(details + details) #TypeError'''

#Dictionary is a Mutable collection
details['marks'] = [25,20,18,20]
#print(details)
#print(len(details))
#in above way we can insert new data into the dictionary

#Methods on Dictionaries:

#print(dir(details))
print(details.keys()) #returns Dictionary Keys
#print(details.values()) #returns Dictionary values
#print(details.items())  #returns Key value pairs from the dictionary

#print(details['id']) #KeyError -->as the key is not present

#print(details.get('ids'))

#print(details.get('id')) #as the key is not present it returns None

#Inserting multiple keys into the dictionary
data = {'email_ids':['nkt@gmail.com','dpt@icloud.com',
                     'vny@yahoo.com','tej@gmail.com'],
        'linkedin_ids':['nkt_123','dpt_234',
                        'vinay345','tej13']}
details.update(data)
#print(details.keys())

#Delete data from the dictionary
#pop(key) -->removes specified data from the dict
'''
print(details.pop('marks'))
print(details.keys())
print(details.popitem()) #removes and returns key value pair from last
print(details.clear())
print(details)

#del details[['marks','ids']] #not possible
del details['marks'],details['ids'] #to delete multiple pairs ata time
print(details.keys())
'''
#print(details.keys())

#setdefault() -->inserts key  into the dictionary if its not present

details.setdefault('status')
#print(details.keys())
#print(details)
details['status'] = ['Placed','Active','OnHold']

#print(details.setdefault('ids')) #aswe already have ids in dictionayry
#its just prints the values
print(details.keys())

#fromkeys() -->create a new dictionary from an iterable
'''
duration = [35,30,65,30]
data = dict.fromkeys(duration)
#data = dict.fromkeys(duration,['Flask','SQL','FastAPI']) #we get 3 keys only as 30 is present
#2 times
print(data)
data[35] = 'Python'
data[30] = 'MYSQL'
print(data)

name = dict.fromkeys('Codegnan')
print(name)
'''
#Nested Dictionaries -->A dictionary inside another dictionary

Students = {'s1':{'Name':'Sai',
                   'ID':'CGVI0240',
                   'batch':'PFS-VSP-007'},
             's2':{'Name':'Raj',
                    'ID':'CGVI0245',
                    'batch':'PFS-VSP-008'}}
'''print(Students)
print(len(Students))
print(Students.keys())
print(type(Students['s1'])) #returns dictionary
print(Students['s1'].keys())

print(Students['s1']['ID'])

#For student s1 update subjects,marks (two new keys to be created)
#Students['s1'].update({'subjects':['Python','Java'],'marks':[95,86]})
#print(Students['s1'])

Students['s1']['subjects'] = ['Python','Aptitude','SS']
Students['s1']['marks'] = [20,20,25]
print(Students['s1'])

#Task: Create your Student Profile with fields as ID number
#Email id,Mobile Number,Parent Whatsappnumber,subjects,
#batch no,daily exam marks,weekly exam marks,batch rank,
#githuburl,linkedinid

Make sure you apply methods also to it(Lists/Sets)
'''
#FrozenSets --> Frozensets are Unordered,it also an Immutable
#collection

data = frozenset()
#print(data)
#print(type(data))
data = frozenset(['Saketh',32,'Codegnan','Vizag'])
print(data)
print(type(data))
print(len(data))
print(data.union(data)) #within itself but no change
print(data.union({'Python','Aptitude'})) #we are passing a set to it
del data   #we can completely remove the collection
#print(data)











































































































