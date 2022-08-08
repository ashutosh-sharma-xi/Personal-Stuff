
"""
#program1
print('enter a positive intiger')
a = int(input())
while a < 0:
    print('error- enter number again')
    a = int(input())
factorial = 1
for i in range(1,a+1):
    factorial = factorial * i
    
print(factorial)  
"""  
# program 2    enter a number to see all pytharorian triplet inside that number

num1 = int(input('enter a number'))
print("pythagorean triplet upto",num1, "are")
for i in range(1,num1+1):
    for j in range(1,i):
        for k in range(1,j):
            if i**2 == j**2 + k**2:
                print(i,j,k)
    




