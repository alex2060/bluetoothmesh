import subprocess
import time

seach_term="abcde"
value_store=[0]*10
counter=-1
value=10
mytime=11
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
    try:
        letsgo=here[1].split("\\t")
        myvar=letsgo[2]
        print(myvar)
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
                counter=counter+1
                if counter==value:
                    x=100
                    mytime=0
                print("added")
                print(value_store)
                print(counter,value)
            else:
                print("in there already")
                print(counter,value)
                if counter==value:
                    x=100
                    print("end")
                    mytime=0

                
                
            
        print(here)
    except:
        pass
    print(counter,value)
    if counter==value:
        x=100
        print("end")
        mytime=0

print(value_store)
final_output=""
for x in range(9):
    try:
        for y in range(7,len(value_store[x])):
            final_output+=value_store[x][y]
    except:
        pass
print("done")
print(final_output)






