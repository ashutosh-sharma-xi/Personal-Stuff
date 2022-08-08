'''
#lambda functions
 # function to add 2 numbers
summ = lambda a,b: a + b
print(summ(5,5))  

# lambda filter() #syntax: filter(lambda(stmt, obj))
# lambda map()  #syntax: map(lambda(stmt, obj))
# lambda reduce()   #syntax: reduce(lambda(stmt, obj))

lst = [1,2,3,4,5,6,7,8,9,10]

#filter 
filterodd = list(filter(lambda i: i%2 != 0,lst))

print(filterodd)

# map
mapodd = list(map(lambda i: i%2 != 0,lst))

# reduce 
# reduce function is not a builtin function in python, it is present in functools module
# reduce() is used for basically  functions like max, min, sum and comprehensions

import functools
summ = functools.reduce(lambda a,b: a+b,lst)
print('the sum of lst is: ' + str(summ))

minn = functools.reduce(lambda a,b: a if a<b else b,lst)
print('the minimum of lst is: ' + str(minn))

maxx = functools.reduce(lambda a,b: a if a>b else b,lst)
print('the maximum of lst is: ' + str(maxx))
'''



