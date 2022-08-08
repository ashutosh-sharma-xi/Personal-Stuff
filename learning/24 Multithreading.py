# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:34:55 2021

@author: Ashutosh
"""
import threading   # Builds on the thread module to more easily manage several threads of execution

# Multitasking - Capability of performing different task at same time
'''
1-Process-based - when two or more processes are running concurrently that is called process based multitasking
eg- in a operating system, playing songs, surfing on web, transferring files simultaneously

2-Thread based - when two or more tasks of a single process or a single program works independent of other tasks
eg- in a game sounds effect, display, etc 
'''

# What is a thread 

# multi-threading
# when we want to run more than one function at a same time this can be done by multi-threading

class Thread1(threading.Thread):
    def run(self):
        for i in range(0,10):
            print(' running')

class Thread2(threading.Thread):
    def run(self):
        for i in range(10,20):
            print(' still running')

class Thread3(threading.Thread):
    def run(self):
        for i in range(20,30):
            print(' now to running')

t1 = Thread1()
t1.start()


t2 = Thread2()
t2.start()

t3 = Thread3()
t3.start()









