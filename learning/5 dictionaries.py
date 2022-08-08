# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:19:02 2021
@author: ashutosh
"""
#dictionaries are nothing but a key value pair
# creating dictionaries
dict1 = {'key1':"value1", 'key2': "value2", 'key3':"value3"}
print(dict1['key1']) # print particular keys
print(dict1) # print whole dictionary

# dictionary inside dictionary
dict2 = {1 :'tnl',2 :['aman','ashutosh','aryan'],3 :{'management':['director','hod','osd']}} 
print(dict2)

# retriving particular values from list inside a dictionary
print(dict2[3]['management'][1])

#assigning values of dictionary to a variable
a = (dict2[3]['management'][0])
b = (dict2[3]['management'][1])
c = (dict2[3]['management'][2])
print(a.upper() + " " + b.upper() + ' ' + c.upper()) 

# assigning new keys and values to a predefined dictionary
#dict1['key3'] = 'value3'   
# or this can be done by update function
dict1.update({'key3': 'value3'})
#print(dict1)

# Deleting key and assigned values of any dictionary
#del dict1['k3']

# to see all the keys of a current dictionary
#print(dict1.keys())

# to see all the values of a current dictionary
#print(dict1.values())

# to see all the pairings of keys and values of a current dictionary
#print(dict1.items())

# assigning a copy of a dictionary to another variable
dictcopy = dict1.copy()

# retriving value from key
print(dict2.get("1"))

#create dictionary from string
st = 'aeiou'
dict3 = {}.fromkeys(str)

# creating a new ditionary

groups = {'group1':["ashutosh","aman","aryan"],'group2': ['tushar','shatabdi','lokesh','nazeer']}
groups['group3'] = ['director','hod','osd']
print(groups['group3'][2])

#  CRUD functions
#  C: create  
#  R: retrieve .get() function
#  U: update    .update() function
#  D: delete     popitem() function - deletes last key value pair of the dictionary
#                  pop() this function deletes the specific key value pair inside parenthesis
# len() function in dictionary gives number of key value pair inside the dictionary


# suppose when there is a list or tuple and we want to create a dictionary from it such that each list element should become a key of dictionary 
# and a default value could be assigned to it by fromkeys() function

# L = [1,2,3,4,5]
# dict = {}
dict.fromkeys(L , default_value)



	
	














