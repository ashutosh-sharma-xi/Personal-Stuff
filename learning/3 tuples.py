
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 01:21:58 2021

@author: ashutosh
"""

# tuples are very similar to lists the differnce between list and tuples is that tuples are immutable.

# lists are created inside square braces whereas tuples are created inside small braces

#creating tuples
my_list = [1,2, 'ashu']   # this is a syntax of a list(mutable)
my_tuple = (1,2,3)         #this is a syntax of a tuple(immutable)
hero = 1 , 'knot'
blank_tuple = ()  
print(type(my_tuple))
print(type(hero))
 
t = ('a','b','c')
print(t.count('a'))

print(t.index('a'))



#________________________________________________________________________________
# how to assign value of one variable to another variable ( for example)

a = "one"
b = "two"

# making b=a and a=b

# temp = a
# a = b
# b = temp

# or

a,b = b,a 

print(a)
print(b)
#_______________________________________________________________________________













