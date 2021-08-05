import subprocess 
import time
import math
import sys
import aes

#QQQQ9112345678910111213
#"spname12345678910111213"

						#id  #binnumber  #key               # message                 #send time     
# python3 sender2.py AbCdEEa 3 bcdefghijklmnapa heyheyitsmewe_gotit_acrosss 20



hey=sys.argv[1]

out=sys.argv[2]

key = sys.argv[3]

intputsting=sys.argv[4]



#sys.argv[2]




array=[]
if len(intputsting)<120:
	stingholder=""
	for x in range(len(intputsting)):
		stingholder=stingholder+intputsting[x]
		if len(stingholder)==12:
			array.append(stingholder)
			stingholder=""
	if stingholder!="":
		for x in range(12-len(stingholder)):
			stingholder=stingholder+"_"
		array.append(stingholder)



endingdata="123456"

for x in range(int(sys.argv[5])):
	for y in range(len(array)):
		#call to name change bluetooth
		namechange=hey+str(len(array)-1)+str(y)+""+array[y]+out
		#print(namechange)
		#message="aBCDEFGHIJKLMNOPQRSTU3"
		myval=aes.encript(key,namechange)
		ret=  aes.decript(key,myval)
		#print(namechange)
		#print(ret)

		subprocess.run("python3 lets_go.py "+myval+endingdata,shell=True)
		time.sleep(45)
