# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 18:51:28 2021

@author: Ashutosh
"""
import time
# inheritance 
"""inheritance means when properties of one class are given to another class
Here one class is called parent class or base class and to whon the properties are given are
called child class
"""

# they are of 4 types in python



"""
1- SINGLE LEVEL INHERITANCE
Here one parent class is inherited to only one child class
"""
class parent:
    name = 'parent'
    def born(self):
        print(time.time())
        
    
class child(parent):    # here only parent class variables are inherited to this class
    name = 'child'
    def born1(self):
        print(time.time())

"""

#-----------------------------------------------------------------------------


2- MULTI LEVEL INHERITANCE
here one parent class is inherited to one child class and this happens in a chain
"""
class automobile:
    name = 'all automobiles'
    def born(self):
        print(time.time())
        
    
class heavyvehicle(automobile):           # all automibile class variable are inherited
    name = 'all heavy vehicles'
    def born1(self):
        print(time.time())
        
class truck(heavyvehicle):                # all automibile class and heavy vehicle variable are inherited
    name = 'all trucks'
    def born1(self):
        print(time.time())
"""

#-----------------------------------------------------------------------------



3. MULTIPLE INHERITANCE
Here one parent class is inherited to multiple child class
"""
class books:
    name = 'all about books'
    pages = 100
    def pages(self):
        print(books.pages)
        
    
class science_books(books):           # all books class variable are inherited
    name = 'all about science books'
    def physics(self):
        print('physics book')
        
class maths_books(books):                # all books class variable are inherited
    name = 'all about maths books'
    def calculas(self):
        print('calculas book')
"""

#-----------------------------------------------------------------------------


4. HIERARCHICAL INHERITANCE
Here multiple parent class is inherited to only one child class 
"""
class mom:
    name = 'jaya bhaduri'
    def family_name(self):
        print(mom.name.split[1])
        
    
class dad:                                        
    name = 'amitabh bachchan'
    def family_name(self):
        print(dad.name.split[1])
        
class son(mom,dad):                                # Both mom and dad class variable are inherited
    name = 'abhishek bachahan'
    def family_name(self):
        print(son.name.split[1])


#==============================================================================

# ABSTRACTION

'''
the process by which we grant permission of what methods or variable when calling
is called abstraction
we can hide or show the variables by abstraction
to make a variable private use __ in front of its name when assigning values
'''
 
class sample_products:
    __product1 = 'deo'
    __product2 = 'computer'
    __product3 = 'oil'
    
    def all_products(self):
        print(sample_products.product1, sample_products.product2, sample_products.product3)


result = sample_products()
print(result.__product1)     # it will show error that no such variable exists because its private
print(result.__product1)     # same here

result.all_products()        # here those variable will be called 

#=============================================================================

# Encapsulation 
'''encapsulation is nothing but binding of different variables and methods 
same as a class. a class is also an example of encapsulation
'''

#=============================================================================

# POLYMORPHISM 
'''poly = many , morphism = forms
polymorphism is the process of implementing two or more methods with same name and different behaviour.
there are generally 2 types of polymorphism

1- method overloading :  process of defining 2 or more method with same name and diferent behaviour

2- method overriding  : process of defining 2 or more methods with same name and also with same behaviour.
'''


def function():
    pass




#=============================================================================
# Ducktyping Philosophy
''' as python is a dynamically typing language it understands by itself what type of variable is there based on its
value, this concept is derived from ducktyping philosophy
 
'''
class duck:
    """docstring for duck"""
    def talk(self):
        print('quack quack')

class man:
    """docstring for man"""
    def speak(self):
        print('hie hello')

class dog(object):
    """docstring for dog"""
    def bark(self):
        print('bow bow')

def display(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'speak'):
        obj.speak()
    elif hasattr(obj,'bark'):
        obj.bark()

for i in (duck(),man(),dog()):
    display(i)

""" 
other such functions are also there like 
getattr()  : used to access the attribute of the object
delattr()  : used to delete a attribute of a object
setattr()   : used to set a specific value to a specific attribute of a object
"""
#----------------------------------------------------------------------------------------------------






