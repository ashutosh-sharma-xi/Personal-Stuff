lst = ['a','b','c','d','e','f','g','h','i']
'''
odd_function = list(map(lambda a:  a% 2!= 0 and a  ,lst))
print(odd_function)
'''
'''
a= ''
for i in lst:
	a = ' '.join(i) if i in ('a','e','i','o','u')  else None
print(a)
'''
'''
#test for prime 
prime_lst = []
prime = lambda a: [ for i in range(fro,to)]

fro = int(input())
to = int(input())
for i in range(fro,to):

'''
'''
# numpy

import numpy as np

arr1 = np.zeros((2,4), dtype = int)

print(np.full((2,4),0,dtype = float))

print(arr1)

# Calculate the cube of all numbers from 1 to a given number

print([i**3 for i in range(1,int(input('enter a number: '))+1)])

'''
"""# febonacci series
num = int(input('enter a number upto which you want series: '))
lst = [1,1]
for i in range(1,num) :
	lst.append(lst[i] +lst[i-1])
print(lst)	
"""


### febonacci series

# num = int(input('enter a number upto which you want series: '))
# lst = [1,1]
# for i in range(1,num) :
# 	lst.append(lst[i] +lst[i-1])
# print(lst)	


# lst = [1,1]
# [lst.append(lst[i] +lst[i-1]) for i in range(1,int(input('enter a number: ')))]
# lst




















