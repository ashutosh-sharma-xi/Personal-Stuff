# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 19:16:48 2021

@author: Ashutosh
"""

# some functions
#--------------------------------------------------------------------------------------------------------
dir()    # returns all the variables inside the python file.

#==========================================================================================================
'''The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
The enumerate() function adds a counter as the key of the enumerate object.

Syntax
enumerate(iterable, start)

listt = ['ashu', 'prachi','cheeku']
print(enumerate(listt, 1))

output - [(1,'ashu'),(2,'prachi'),(3,'cheeku')]

lst = [1,2,3,4,5]
for i in enumerate(lst):        # returns element along with their index number
    print(i)

#========================================================================================================
assert len(lst) > 4             # assert() function works as if statement and its easy to use
try:
    print(max(lst) * 2)
except Exception as e:
    print(e)

'''
#=========================================================================================================
# *args and **kwargs
'''
*args are used when we use a function and take a fixed number of arguments, but if somehow you need to 
reduce or increase the number of variables then you need to change it everywhere at the function to
this problem can be resolved by args 
**kwargs when your data structure is a dictionary and you want to take its key-value pair as argument in 
this we can use **kwargs

note: its not mandatory to use args or kwargs as they are not keywords, they are just commonly used words
we can use any word there but * / ** is compulsary
'''
# *args

heroes = ['amitabh','salman','shahrukh','hritik','akshay']   # a list where we can modify the values and the functionality will not affect
def about_heroes(*args):             # defining a function where *args is used
    for arg in args:
        print(arg, ' is a hero')

about_heroes(*heroes)                  

# **kwargs
homes = {'dog':'kennel','horse':'shed','lion':'den','human':'home'}

def my_sweet_home(**kwargs):
    for key,value in kwargs.items():
       print(f'{key} lives in a {value}')

my_sweet_home(**homes)

#==========================================================================================================

#==========================================================================================================

#==========================================================================================================

#==========================================================================================================

#==========================================================================================================

#==========================================================================================================

#==========================================================================================================





















