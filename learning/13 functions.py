# -*- coding: utf-8 -*-
"""
Created on Sun May 16 15:16:09 2021

@author: ashutosh
"""


def summ(a,b):   # functions are defined through 'def' keyword
     """
     function for sum of 2 digits
     """
     return a+b            # 'return' keyword allows you to return the value of function ie.(in a variable)
   
print('enter first number')
a = int(input())

print('enter second number')
b = int(input())

h = summ(a,b)            # invoked user defined function 'summ'
print(h)
# to see the docstring 
print(summ.__doc__)

# ARGUMENTS-  the value that we pass for the execution ie. 1,5,12
# PARAMETERS- the values that we define in the function ie. a,b, num



def door(Open,Close):
    if Open == True:
       stmt = 'door open'
    elif Close != True:
       stmt = 'door closed'
    else:
       stmt = 'fuck off'
    return stmt
        
a= door(False, True)
print(a)        

st = 'string'
num = 1
tup = 1,2,3
li = [1,2]
dic = {1:[1,2,3]}
sett = set()

print(dir(st)) # dir() function is used to show all the methods of the given datastructure

# Recursive functions
# A recursive function is a function defined in terms of itself via self-referential expressions


def factorial(num):
    if num > 0:
        result = int()
        for i in range(1,num):
            result = result *i
    elif num < 0: 
        factorial((-(num+num+num)))          # as here function is used inside itself

    return result    


factorial(3)








