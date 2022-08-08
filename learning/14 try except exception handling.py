import random 
# try except exception handling
print ('hello how can i help you')
print('1- play guess a number game \n  2- play a song')
num = int(input('enter a number'))
# try statement will execute the following set of code inside it and then further except is used for except exception
try:
	if num == 1:
		guess = random.randint(10,20)
		chances = 5
		print('ENTER A NEW NUMBER')
		for i in range(0,5):
		    num = int(input())
		    chances = chances - 1
		    if num > guess :
		        print('enter smaller number',chances,'chances left')
		    elif num < guess:
		        print('enter larger number',chances,'chances left')
		    elif num == guess:
		        print('correct number "you won"')
		        print('your score =',(chances+1)*10)
		        break
		if chances == 0 and num != guess:
		     print('YOU LOST!')
# except exception will allow the further code to run without being interupted by the error		     
except Exception as e :  
	print(e)

#except:                    # this is a user defined exception
#	print('error')

else:
	('try executed so this else is executed')

finally:
	print('jai shree Ram')




































