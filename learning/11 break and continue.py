# -*- coding: utf-8 -*-
"""
Created on Wed May 12 00:24:20 2021

@author: ashutosh
"""

# break keword is used to stop the execution of the code after a certain point
a = int(4)
while a<100:
    print(a)
    a=a+1
    if a**2 == 25:
        break
print('done')

# True or 1 inside creates a never ending loop
"""
while (True):
    print('ashutosh')
"""
"""continue statements are used when a given set of 
condition is true till then the above code execute else it will run further loop"""

a= 10
for i in range(1,a):
    if i < 5:
        continue
    print(i)
    
print('loop ended')    






































