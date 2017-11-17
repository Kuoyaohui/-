import os

haha = input()
tt1=str(haha)
#kkk=str(haha)
kkk='hello'


try:
	with open('C:/Users/a9890/Desktop/'+tt1+".txt",'w') as fo:
		fo.write(kkk)
except IOError as err:
	print(err)
finally:
	fo.close()

