import subprocess
import time
import aes
seach_term="AbCdEEa"
#AbCdEEa 3 bcdefghijklmnapa
keyval="bcdefghijklmnapa"
value_store=[0]*10
back_bite=[0]*10
backpublic=[0]*10
counter=-1
value=10
mytime=11
backbits=""
for x in range(40):
    command = ['hcitool', 'scan']
    if mytime!=0:
        p = subprocess.check_output("hcitool scan", shell=True)
    #print("scan")
    time.sleep(mytime)
    here=str(p)
    print("next scan")
    here=here.split("\\n")
    print(here)
    print("in here")
    try:
        letsgo=here[1].split("\\t")
        myvar=aes.decript(keyval,letsgo[2])
        pivar=""
        backbit=""
        print(letsgo[2])
        for x in range(len(myvar)-1):
            pivar=pivar+myvar[x]
        
        backbit=myvar[21]
        oldvar=myvar
        myvar=pivar
        lastbits=letsgo[2][22:]
        
        print()
        print(oldvar)
        print()
        print(myvar)
        print()
        print()
        print()
        print()
        true_value=1
        for k in range(len(seach_term)):
            print(myvar[k],seach_term[k])
            if myvar[k]==seach_term[k]:
                pass
            else:
                true_value=0
        print(true_value)
        if(true_value==1):
            print(myvar)
            print(myvar[len(seach_term)+1])
            print(value_store[int(myvar[len(seach_term)+1])])
            mytest=value_store[int(myvar[len(seach_term)+1])]==0
            print(mytest)
            if mytest:
                value=int(myvar[len(seach_term)])
                value_store[int(myvar[len(seach_term)+1])]=myvar
                back_bite[int(myvar[len(seach_term)+1])]=backbit
                backpublic[int(myvar[len(seach_term)+1])]=lastbits
                counter=counter+1
                if counter==value:
                    x=100
                    mytime=0
                print("added")
                print(value_store)
                print(counter,value)
            else:
                print(value_store)
                print(counter,value)
                print("in there already")

                if counter==value:
                    x=100
                    print("end")
                    mytime=0
                    

                
                
            
        print(here)
        print(counter,value)
        if counter==value:
            x=100
            print("end")
            mytime=0
    except:
        pass
print(value_store)
final_output=""
for x in range(9):
    try:
        for y in range(9,len(value_store[x])):
            final_output+=value_store[x][y]
    except:
        pass
print("done")
print()
print()
print()
print()
print()
print()
print(final_output)
print()
print(back_bite)
print()
print(backpublic)
print("letsgo")





