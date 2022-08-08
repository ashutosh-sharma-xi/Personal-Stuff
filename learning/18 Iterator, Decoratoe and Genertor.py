# ||ITERATORS||
#  next()
# iter()

inp = eval(input())
if inp % 2 ==0:
    print('even')
    iter('even')
else:
    print('odd')
    iter()

# ||DECORATORS||
# Decorator is a function which decorates another function without changing the function itself

import time
def squares(lst):
    resultList = []
    start = time.time()
    for i in lst:
        resultList.append(i*i)
    end = time.time()
    duration = end-start
    print('The Squares Function is Taking',round(duration,2),'secs.')
    return resultList

def cubes(lst):
    resultList = []
    start = time.time()
    for i in lst:
        resultList.append(i*i*i)
    end = time.time()
    duration = end-start
    print('The Cubes Function is Taking',round(duration,2),'secs.')
    return resultList

lst = range(1000000)
sResult = squares(lst)
cResult = cubes(lst)

#=====Another Example of Decorator=====#


def design(ashutosh):
        def presuf():
                print('Boss')
                ashutosh()
                print(time.time())
        return presuf

@design
def ashutosh():
    print('Ashutosh')

#ashutosh = design(ashutosh)    # uncomment this if @design is removed  both have same functionalty
ashutosh()

#||GENERATOR||


# A generator is used to get iterable items but it does'nt print it or used ram.
# it is used to generate such items, it is generated using yield() function

 
def upto(n):
    for i in range(n):
        yield i
    

# print(upto(50))  # this will print that a generator is generated upto a limit

# to get items from generator first we'll create a variable and store values of upto function in it and use next() keyword

nums = upto(50)

print(next(nums))  # this will print 0 
print(next(nums))   # this will print 1
print(max(nums))    # this will print 49

# after a limit the generators close working this means it only gives a few iterables them it shows error 
# as in next() after a few next() function they will give error
print(type(nums))


