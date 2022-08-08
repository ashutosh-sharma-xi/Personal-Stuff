# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 19:39:38 2021

@author: ashutosh
"""

# ALL ABOUT LISTS

# CREATING LISTS
MY_LIST_1 = [3, 2, 1]
MY_LIST_2 = [4, 6, 5]
#print(MY_LIST_1)             #print1

# length of LIST
#print(len(MY_LIST_1))   #print2

# Indexing of lists
#print(MY_LIST_1[1::])   #print3
#print(MY_LIST_1[0:2])   #print4
#print(MY_LIST_1[1::])   #print5

#print(MY_LIST_1[0])      #print6
#print(MY_LIST_1[:1:])      #print7
#print(MY_LIST_1 + MY_LIST_2[1:])    #print8

New_list = MY_LIST_1 + MY_LIST_2       # packing of MY_list_1 and MY_LIST_2 in New_list
print(New_list[::-1])               #print9 slicing in lists 

New_list.pop()                        #print10  pop function removes the last character of the list

New_list.append(5)                     #print  append function adds up an element to the last place of the list

New_list.sort()                          #print sort function sorts the list in ascending order

New_list.reverse()                         # reverse function reverses the queue of the list

New_list.insert(2, 9)                        #print  insert function inserts a element on a desired index
 	
New_list.remove(9)                              #print remove function removes the given value from the given list

New_list.length()                                 #  retrives the length of the list

New_list.count(1)                                   # counts the particular element is repeated how many times in the list

New_list.index(3)                                     # gives the index value of given number inside index function 

New_list.clear()                                        # clear whole elements inside list

New_list.delete()                                          # delete the whole list
   
#print(type(New_list))

 
Listx = ["1","2",["c","d"]]
#print(Listx)
 
#print(Listx[2[0:5]])

numbers = [1,2,4,3,5,8,6]
print("the smallest number is", min(numbers))          #print min function or max function gives the smallest/largest value of the list 


lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = [7,8,9]

listt = [lst1,lst2,lst3]              # will create a new list containing 3 lists










































