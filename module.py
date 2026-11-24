'''
Modules -->User Defined Modules --> Create,Accessing..
Built-in Modules --> math,os,sys,time....
A Module is a Python file(.py) consists of objects,variables,functions
we use import keyword..

import mymodule
print(dir(mymodule)) #use dir to get list of all available methods and attributes
print(type(mymodule.greet))
print(mymodule.greet("Saketh"))
print(type(mymodule.names))
print(mymodule.names.items())

print(mymodule.__doc__) #returns docstring (description of module)
print(__doc__) #returns current file docstring

mymodule.names.update({"Place":"Vizag","subjects":['Python','Aptitude',
                                                   'SQL']})
print(mymodule.names)
print(len(mymodule.names))

#Accessing methods/attributes using from keyword
from mymodule import greet
print(greet("Codegnan"))

#print(names) #this is not possible as we didn't import it
from mymodule import greet,names #we can import multiple attributes
print(names)

#Aliasing module names
import mymodule as me
print(me.greet("Vijay"))
print(me.names.keys())
'''
#To access all methods/attributes we use '*'
from mymodule import *   #this is only recommended for user/simple modules
print(names)
print(greet("Saketh"))
f = display()
print(next(f))








































