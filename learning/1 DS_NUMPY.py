# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:37:30 2021

@author: Ashutosh
"""

# all about numpy

import numpy as np

array1 = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]], dtype = int)        # in list format can also take tuple

print(array1)

array2 = np.ones((2,5))
print(array2)

array3 = np.zeros((2,5))
print(array3)

array4 = np.full((2,5),3)
print(array4)

array5 = np.random.random((2,5))
print(array5)

array6 = np.arange(0,20,2)               # same as range function
print(array6)

array7 = np.linspace(1,10,2)
print(array7)

array8 = np.empty((2,4))
print(array8)

array9 = np.empty_like(array1)
print(array9)
 
array10 = np.identity(10)                  # will give array of 10*10
print(array10)

array11 = np.eye(2)                   #Create a 2X2 identity matrix

print(type(array1),type(array2),type(array3))


# numpy array functions
print(array1.shape)             
print(array1.size)           
print(array1.dtype)            
print(array1.ndim)              
print(array1.itemsize) 
print(array1.reshape(3,3))   #Reshape, but don’t change data
print(array1.ravel())        # makes the array 1 dimentional
print(array1.sum(axis = 0))  # sum of vertical axis
print(array1.sum(axis = 1))  # sum of hrizontalal axis
print(array2.T)              # transpose
print(array1.flat)          
for item in array2.flat:
    print(item)
print(array1.nbytes)
print(array2.argmax())            # return index of largest element
print(array1.argmax(axis = 0))    # used for 2 dimensional array
print(array2.argmin())            # return index of smallest element
print(array2.argsort())           # returns the sorted index
print(array2.min())
print(array2.max())
print(np.where(array2>4))      # np.where gives value based on condition
print(np.count_nonzero(array2))  # returns number of non zero in the array
print(np.nonzero(array4))        # returns dimention where non zero element present
print(array1.tolist())         # converts array to python list
ar_copy = np.copy(array4)      # copies the array (no changes made in copied or original array when changes done in any array )
ar_view = np.view(array4)      # creates a view of the array ( when we modifies either original or new variable, changes takes place in both) 
print(np.sort(array4,axis = 0))  # sorts the array based on axis(0 - column, 1 - row, default is 1)
new_array = np.append(array4,5)  # can also take an another array in place of 5
new_array2 = np.insert(array7,3,200).reshape(1,6)  # insert element at a specific place
np.delete(new_array2,200)        # delete 200 from new_array2 (we can also specify axis)
np.concatenate(new_array,new_array2)   # concatenate two or more arrays (we can also specify axis --default: axis = 0)
print(np.hstack((array4,array5)))      # horizontally stacks arrays
print(np.vstack((array4,array5)))      # vertically stacks arrays
array1.resize((2,6))                    #Return a new array with shape (2,6)


#-----------------------------------------------------------------------------
# Numpy Broadcasting 

#--------------------
# performing arithmetic operation on arrays

ar1 = np.array([1,2,3,4])
ar2 = np.array([2,4,6,8])
lst = [1,3,5,7]
print(ar1*ar2)

print(ar1+ar2)

print(ar2+lst)

#-----------------------------------------------------------------------------
#  indexing slicing over an array

print(array2[2])
print(array1[2:,2:])
print(array1[...,1:2])
print(array2[[1,0,2],[1,1,2]])

# advanced slicing

rows = np.array([1,2],[1,0])
columns = np.array([1,2],[0,1])

print(array1[rows,columns])

#-----------------------------------------------------------------------------
#Iterating over an array
iter(array1)

np.nditer(array1,opflags=['readwrite'])

#-----------------------------------------------------------------------------
# saving and loading on Disk

np.save('my_array', array10)
np.savez('array.npz', array1, array4)
np.load('my_array.npy')


#saving and loading textfiles

np.loadtxt("myfile.txt")
np.genfromtxt("my_file.csv", delimiter=',')
np.savetxt("myarray.txt", array1, delimiter=" ")


#==============================================================================



























