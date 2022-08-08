 
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:16:30 2021
@author: Ashutosh
"""

# OOPS
# object oriented programming language 

my_current_status = 'i am coding'

class Myclass:
    ''' this is my first class'''           #  docstring
    name = 'Ashutosh'                         # this is a class variable
    profession = 'Student'
    
    def status(self):                      # here this is called a method inside a class 
        return my_current_status  
    
    def strength(self):
        return 'high'

obj = Myclass()               # created object of Myclass() class

print(obj.name)                # calling the class variable
print(obj.profession)

obj.status()                    # calling the status method of object obj of Myclass() class

print(obj.__doc__)             # printing the docstring


#===============================================================================================
# class variable :  if the value is same for all objects then the variable is class variable
# object variable: if the value keep on changing for all the objects then it is called object variable
 
'''for creating object variable we need to create a constructor which is 
initialised by __init__ keyword. whenever we create a class we need to send arguments to the 
constructor compulsarily: example below
'''
class accounts:
    deleloper = 'Ashutosh sharma'             # class variable 
    year = 2021
    
    def __init__(self, variable_cost, fixed_cost, sales ,per_unit_price):   # object variable( fixed cost, sales)
        self.variable_cost = variable_cost                
        self.fixed_cost = fixed_cost
        self.sales = sales
        self.per_unit_price = per_unit_price
        print('Break-even point is', fixed_cost / (per_unit_price - variable_cost))
        
    
    def pv_ratio(self):
        res = (self.per_unit_price - self.variable_cost) / self.per_unit_price
        return res


tata_finance = accounts(30,2000000,800000000,70)             
''' here its compulsarily we need to give arguments for __init__ method (constructor) and whenever 
objects of amy class are created the constructor will run without calling. In this case it will 
run the print statement
'''
#===============An example ====================




class cars:

    def __init__(self,name,milage,topspeed):
        self.milage  = milage
        self.topspeed = topspeed
        self.name = name

    def mycar(self):
        print(f'I have {self.name} car and it provides me a good milege of {self.milage} and topspeed of {self.topspeed} ')

fortuner = cars('fortuner',14,170)

print(fortuner.mycar())



#============================================================
# types of Methods
'''
1. Instance methods: if we use self argument in the implementation
 of any method that method is called Instance Method'''
'''

2. class Methods: when classes are created by cls keyword'''

class study:
    @classmethod
    def class_method(cls):
        inp = input('enter a string')
        if inp == 'class':
            print('its class')
        else :
            print('not class')


    '''
    3. Static Methods: when method is created without cls or self keyword
    '''
    @staticmethod
    def static_method():
        inp = input('enter a string')
        if inp == 'static':
            print('its static')
        else :
            print('not static')

study.static_method()
study.class_method()



# Taking input from user in the class

class students():
    def __init__(self, name, marks,location, college ):
        self.name = name
        self.marks = marks
        self.location = location
        self.college = college
        
    def percentage(self):
        return (self.name,'got', self.marks/5, 'percentage')

for i in range(int(input())):
    name = input('enter name')
    marks = input('enter total marks')
    location = input('enter location')
    college = input('enter college name')
    students(name,marks,location,college)
    students.percentage()


# Taking data from database 
import pymysql
connection = pymysql.connect(host= 'localhost', 
                             user = 'root',
                             password= 'ashu',
                             db = 'python')

c = connection.cursor()
sql = 'select * from students'
c.execute(sql)
data = c.fetchall()

# taking input by files
