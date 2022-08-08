# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 19:20:25 2021

@author: Ashutosh
"""

import unittest
import logging    # used for logging of program data


def add(a,b):
    c = a+b
    return c

def sub(a,b):
    c = a-b
    return c

m= 15
n= 5

class function_testing(unittest.TestCase):
    def add_test(self):
        self.assertEqual(add(m,n),20)
        
    def sub_test(self):
        self.assertEqual(sub(m,n),10)

unittest.main()      # for testing all functions inside class function_testing


call = function_testing()
call.add_test()                # for testing specific function inside class function_tesing()

print(add(m,n))
print('the sum of {} and,{} is {}'.format(m,n,add(m,n)))

#=============================================================================

# LOGGING 

# Logging is the process of tracking log data in log file
# log data means when the program working started when it stopped etc in a file called log file

# debug - If we are sure that the program will never fail
# info - If we are sure that the program will not fail, but have little doubt
# warning - Program currently working fine but it may fail i near future
# ERROR - If any program may return error, then we specify error
# CRITICAL - when the program may return error and cause fail to entire project, then we specify critical


logging.debug('the sum of {} and,{} is {}'.format(m,n,add(m,n)))
logging.info('the sum of {} and,{} is {}'.format(m,n,add(m,n)))
logging.warning('the sum of {} and,{} is {}'.format(m,n,add(m,n)))
logging.error('the sum of {} and,{} is {}'.format(m,n,add(m,n)))
logging.critical('the sum of {} and,{} is {}'.format(m,n,add(m,n)))





































