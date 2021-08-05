from Crypto.Cipher import AES





def messagepaker(message):
	output=""
	for x in range(len(message)):
		output=output+message[x]
		if len(output)==21:
			return output
	for x in range(21):
		output=output+"_"
		if len(output)==21:
			return output



def point_to_value(a):
	if a=="0":
		return 0
	if a=="1":
		return 1
	if a=="2":
		return 2
	if a=="3":
		return 3
	if a=="4":
		return 4
	if a=="5":
		return 5
	if a=="6":
		return 6
	if a=="7":
		return 7
	if a=="8":
		return 8
	if a=="9":
		return 9
	if a=="a":
		return 10
	if a=="b":
		return 11
	if a=="c":
		return 12
	if a=="d":
		return 13
	if a=="e":
		return 14
	if a=="f":
		return 15
	if a=="g":
		return 16
	if a=="h":
		return 17
	if a=="i":
		return 18
	if a=="j":
		return 19
	if a=="k":
		return 20
	if a=="l":
		return 21
	if a=="m":
		return 22
	if a=="n":
		return 23
	if a=="o":
		return 24
	if a=="p":
		return 25
	if a=="q":
		return 26
	if a=="r":
		return 27
	if a=="s":
		return 28
	if a=="t":
		return 29
	if a=="u":
		return 30
	if a=="v":
		return 31
	if a=="w":
		return 32
	if a=="x":
		return 33
	if a=="y":
		return 34
	if a=="z":
		return 35
	if a=="A":
		return 36
	if a=="B":
		return 37
	if a=="C":
		return 38
	if a=="D":
		return 39
	if a=="E":
		return 40
	if a=="F":
		return 41
	if a=="G":
		return 42
	if a=="H":
		return 43
	if a=="I":
		return 44
	if a=="J":
		return 45
	if a=="K":
		return 46
	if a=="L":
		return 47
	if a=="M":
		return 48
	if a=="N":
		return 49
	if a=="O":
		return 50
	if a=="P":
		return 51
	if a=="Q":
		return 52
	if a=="R":
		return 53
	if a=="S":
		return 54
	if a=="T":
		return 55
	if a=="U":
		return 56
	if a=="V":
		return 57
	if a=="W":
		return 58
	if a=="X":
		return 59
	if a=="Y":
		return 60
	if a=="Z":
		return 61
	if a=="-":
		return 62
	return 63


def value_to_point(a):
	if a==0:
		return "0"
	if a==1:
		return "1"
	if a==2:
		return "2"
	if a==3:
		return "3"
	if a==4:
		return "4"
	if a==5:
		return "5"
	if a==6:
		return "6"
	if a==7:
		return "7"
	if a==8:
		return "8"
	if a==9:
		return "9"
	if a==10:
		return "a"
	if a==11:
		return "b"
	if a==12:
		return "c"
	if a==13:
		return "d"
	if a==14:
		return "e"
	if a==15:
		return "f"
	if a==16:
		return "g"
	if a==17:
		return "h"
	if a==18:
		return "i"
	if a==19:
		return "j"
	if a==20:
		return "k"
	if a==21:
		return "l"
	if a==22:
		return "m"
	if a==23:
		return "n"
	if a==24:
		return "o"
	if a==25:
		return "p"
	if a==26:
		return "q"
	if a==27:
		return "r"
	if a==28:
		return "s"
	if a==29:
		return "t"
	if a==30:
		return "u"
	if a==31:
		return "v"
	if a==32:
		return "w"
	if a==33:
		return "x"
	if a==34:
		return "y"
	if a==35:
		return "z"

	if a==36:
		return "A"
	if a==37:
		return "B"
	if a==38:
		return "C"
	if a==39:
		return "D"
	if a==40:
		return "E"
	if a==41:
		return "F"
	if a==42:
		return "G"
	if a==43:
		return "H"
	if a==44:
		return "I"
	if a==45:
		return "J"
	if a==46:
		return "K"
	if a==47:
		return "L"
	if a==48:
		return "M"
	if a==49:
		return "N"
	if a==50:
		return "O"
	if a==51:
		return "P"
	if a==52:
		return "Q"
	if a==53:
		return "R"
	if a==54:
		return "S"
	if a==55:
		return "T"
	if a==56:
		return "U"
	if a==57:
		return "V"
	if a==58:
		return "W"
	if a==59:
		return "X"
	if a==60:
		return "Y"
	if a==61:
		return "Z"
	if a==62:
		return "-"
	if a==63:
		return "_"

def number_valie(myval):
	array=[0]*6
	if myval>=2**5:
		array[0]=1
		myval=myval-2**5

	if myval>=2**4:
		array[1]=1
		myval=myval-2**4

	if myval>=2**3:
		array[2]=1
		myval=myval-2**3

	if myval>=2**2:
		array[3]=1
		myval=myval-2**2

	if myval>=2**1:
		array[4]=1
		myval=myval-2**1

	if myval>=2**0:
		array[5]=1
		myval=myval-2**0

	return array







def messge_to_cipher(message,b1,b2):
	mess=messagepaker(message)
	array=[0]*16
	for x in range(16):
		array[x]=point_to_value(mess[x])
	counter=0
	for x in range(16,21):
		value=number_valie( point_to_value(mess[x]) )
		array[3*counter+0]=array[3*counter+0]+value[0]*(2**7)+value[1]*(2**6)
		array[3*counter+1]=array[3*counter+1]+value[2]*(2**7)+value[3]*(2**6)
		array[3*counter+2]=array[3*counter+2]+value[4]*(2**7)+value[5]*(2**6)
		counter=counter+1
	array[15]=array[15]+b1*2**7+b2*2**6
	msg2 =bytes([array[0],array[1],array[2],array[3],array[4],array[5],array[6],array[7],array[8],array[9],array[10],array[11],array[12],array[13],array[14],array[15]])
	return msg2


def lets_go(V1,V2,V3):
	mypal=[0,0,0]
	mypal[0]=V1
	mypal[1]=V2
	mypal[2]=V3

	myout=0
	if mypal[0]>=2**7:
		mypal[0]=mypal[0]-2**7
		myout=myout+2**5

	if mypal[0]>=2**6:
		mypal[0]=mypal[0]-2**6
		myout=myout+2**4

	if mypal[1]>=2**7:
		mypal[1]=mypal[1]-2**7
		myout=myout+2**3

	if mypal[1]>=2**6:
		mypal[1]=mypal[1]-2**6
		myout=myout+2**2

	if mypal[2]>=2**7:
		mypal[2]=mypal[2]-2**7
		myout=myout+2**1

	if mypal[2]>=2**6:
		mypal[2]=mypal[2]-2**6
		myout=myout+2**0


	mypal[0]=value_to_point(mypal[0])
	mypal[1]=value_to_point(mypal[1])
	mypal[2]=value_to_point(mypal[2])
	return [mypal,value_to_point(myout) ]

def cipher_to_messge(cyfer):
	array=["+"]*21
	array_second_cyfer=[0]*16
	for x in range(5):
		myholder=lets_go(cyfer[3*x+0],cyfer[3*x+1],cyfer[3*x+2])
		array[x*3+0]=myholder[0][0]
		array[x*3+1]=myholder[0][1]
		array[x*3+2]=myholder[0][2]

		array[16+x] =myholder[1]

	lastval=cyfer[15]
	exex=0
	if lastval>=2**7:
		lastval=lastval-2**7
		exex=exex+2**1

	if lastval>=2**6:
		lastval=lastval-2**6
		exex=value_to_point(exex+2**0)
	array[15]=value_to_point(lastval)
	out=""
	for x in range(len(array)):
		out+=array[x]
	return out+str(exex)








key = 'bcdefghijklmnapa'

cipher = AES.new(key, AES.MODE_ECB)


msg1 = cipher.encrypt(	messge_to_cipher("ABCDEFGHIJKLMNOPQRSTU",1,1)		)


decipher = AES.new(key, AES.MODE_ECB)


def bitless_messge_to_cipher(message):
	#print(message)
	#print(len(message))
	if message[21]=="0":
		return messge_to_cipher(message,0,0)
	if message[21]=="1":
		return messge_to_cipher(message,0,1)
	if message[21]=="2":
		return messge_to_cipher(message,1,0)
	if message[21]=="3":
		return messge_to_cipher(message,1,1)



def encript(key,message):
	cipher = AES.new(key, AES.MODE_ECB)
	msg1 = cipher.encrypt(	bitless_messge_to_cipher(message)		)	
	return cipher_to_messge(msg1)


def decript(key,message):
	decipher = AES.new(key, AES.MODE_ECB)
	return cipher_to_messge( decipher.decrypt( bitless_messge_to_cipher(message) ) )





#message="aBCDEFGHIJKLMNOPQRSTU0"


#mysend= encript(key,message)
#print(mysend)


#ret=	decript(key,mysend)

#print(ret)














