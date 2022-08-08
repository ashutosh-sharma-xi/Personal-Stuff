# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 13:05:02 2021

@author: Ashutosh
"""



def ABcount(s):
	letters = list(s)
	lst = list()
	lst.append(letters[0])
	print(letters)
	for i in letters:
		if i not in lst:
			lst.append(i)
			
	
	
	dic = dict()	

	for n in letters:
		dic[n]= lst.count(n)
		dic.update( [(n, lst.count(n))] )
		
	print(dic)



s = 'abcd'
ABcount(s)










