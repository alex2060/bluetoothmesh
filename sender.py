import subprocess 
import time
import math
#QQQQ9112345678910111213
#"spname12345678910111213"

intputsting="never_going_to_give_you_up_never_going_to_let_you_down_never_going_to"


array=[]
if len(intputsting)<200:
	stingholder=""
	for x in range(len(intputsting)):
		stingholder=stingholder+intputsting[x]
		if len(stingholder)==20:
			array.append(stingholder)
			stingholder=""
	if stingholder!="":
		array.append(stingholder)






for x in range(10):
	for y in range(len(array)):
		subprocess.run("python3 lets_go.py abcde"+str(len(array)-1)+str(y)+""+array[y],shell=True)
		time.sleep(30)


