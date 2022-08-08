# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 19:09:23 2021

@author: Ashutosh
"""

# Regular Expressions 
# Also called RE or Reg Ex

import re
# imp functions of RE 
# match( )  matches the 
# fullmatch( )
# sub( )
# subn( )
# split( )
# findall( )
# search( )
# finditer( )


mystr  = '''hello my name is ashutosh and i am a good
boy i live in india and i am fond of bikes. i am writing this
because i am not in the mood to write but to study re
module i have to type something so is the reason that i
am writing this '''
#----------------------------------



#---------finditer() function------!harrybhai------
# used to find in a string
var = re.compile(r'i')
result = var.finditer(mystr)
for n in result:
    print('fiditer ' , n)

result2 = re.finditer( 'ashutosh\s'  ,mystr)
for n in result:
    print('fiditer ' , n)

#---------split() function------------
spl = re.split(r'\s ',mystr)
print(spl)


#---------findall() function------------
fda = re.findall('\Aa', mystr)
print(fda)

#---------search() function------------
src = re.search('\Aa', mystr)
print(src)

#---------sub() function-----------

sb = re.sub('\s','_',mystr)    # first argument(\s, \W, \w etc)shows character class, second argument contains character to replace by, and third argument contains string)
print('sub ' , sb)

#---------subn() function-----------
sbn = re.subn('\s','_',mystr)  # same as sub() but also counts number of words
print('subm ' , sbn)

#---------match() function-----------
string = re.match(r'\wa?',mystr)
print('match ', string)
if string != 'None':
    print('its a match')
elif string == 'None':
    print('its not a match')

#---------match() function-----------
    
spl = re.split('\n',mystr)
print('split ' , spl)    

#====================
#character classes

"""
predefined characters
======================
  \A - returns a match if the specified characters are at the begining if the string
  \b - returns a match where  the specified characters are at the begining or at the end of the word

   \s - space character
   \S - any character except space character

   \d - any digit from 1-9
   \D - any character expect digit

    \w - any word  character [a-z A-Z 0-9]
    \W - any character except word character (special character)

    .  - any character including special character
    *  - zero or more occurences
    ^  - starts with
    $  - Ends with
    {} - Exactly the specified number of occurence
    |  - Eit her or
    () - capture and group
    r  - raw string used before characters using backslash \ to print x character
         whatever( only used with re)

user defined characters 
=======================
"""
# Quantifiers
#================

"""
a  -----   Exactly one 'a'
a+ ------  Atleast one 'a'
a* -----   any number of 'a' characters including zero number of 'a'
a? -----   atmost one 'a' 
a{m} ------- exactly m number of a's
a{m,n}-------- a minimum m number of times and maximum n number of times
"""


