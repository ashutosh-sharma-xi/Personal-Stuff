#indexing
string = "DingDongDingDongDing" 

nstr = string[4]

#    print(string[0:3])       #print3
#    print(string[3:])        #print4
#    print(string[:3])        #print5
#    print(string[::])        #print6
#    print(string[3])         #print7
#    print(string[3::])       #print8
#    print(string[:3:])       #print9
#    print(string[::3])       #print10
#    print(string[3:5:7])     #print11
#    print(string[::-2])      #print12)

# slicing 
 #   print("ashutosh"[4:])  #print13
  #  print(string[2:6])      #print14
   # print(len(string ))      #print15

txt1 = "ashutosh"
txt2 = "sharma"
 
#concatenation
#print('ashutosh'+ ' ' + 'sharma' ) #print16
 
# string datatypes do not allow value assignment

txt1 = 'A' + txt1[1::] #
print( txt1)  #print17

# concatenating 2 diferrent variables and capittalizing their first term
print("A" + txt1[1::]  + " " + "S" + txt2[1::])  #print18

# multiplication of strings
txt3 = 3 * (txt1 +' ' + txt2 +' ')

FIRSTSTR = 'THIS IS MY FIRST STRING'
print(FIRSTSTR[:-6] +  'text')


a= 'python is the best,language'
b= 'after java'
print(a.isalnum())   #isalnum = is alpha numeric
print(a.isalpha())   # isalpha() = is alphabet  note- spaces are not calculated i alpha or numeric
print(a.endswith('best language'))  # endswith()  = shows the word which ends with it
print(a.endswith('python'))
print(a.capitalize()) # converts first letter of the string to capital
print(a.title())  # converts first letter of all the words to capital
print(a.count('python')) # counts number of charracter
print(a.find('python'))  # returns index number of the word
print(a.lower())
print(a.upper())
print(a.index('a'))
print(a.replace('python','java'))
print(a.split())    # split on the basis of space
print(a.split(',')) # split on the basis of comma
f ='_'.join([a,b])   # join function 
print(f)
print('enter a number', end = "\t")
a = input()
"""
this is a multi line comment (or argument)

"""
#============================================================================

# packing and unpacking strings

st= "hie! "
st1= "ashutosh."
st2= " how are you?"      
      
STR = st + st1 +st2  # packing

a,b,c,d,e,f,g,f = st1   # unpacking. should be equal number of character both      

#=============================================================================

# f-strings and other string formating methods

a,b,c,d = 'ashutosh sharma', 'kumar aman','aryan namdev','yogesh payasi'
e,f,g,h = 'python', 'R','java','ruby'
i,j,k,l = 'kareli', 'ranchi','narsinghpur','bhopal'

# Using .format() method

st1 = 'the name of 4 geeks are {}, {}, {}, {}'.format(a,b,c,d)

# using %s symbol
st2 = 'they are expert users of %s, %s, %s and %s respectively' %(e,f,g,h)

# using f-strings
st3 = f"They belongs from {i}, {j}, {k} and {l} respectively"























