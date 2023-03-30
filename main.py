import time
import pyttsx3
print("1. Alaram \n2. Timer")
print("Enter 1 or 2 :",end=" ")
choice=int(input())
if choice==2:
    print("Enter the time in seconds :",end=" ")
    timer=int(input())
    time.sleep(timer)
    talk=pyttsx3.init()
    voices=talk.getProperty('voices')
    talk.setProperty('voice',voices[1].id)
    talk.setProperty('rate',150)
    talk.say("Time up!")
    talk.runAndWait()
elif choice==1:
    tm={}
    print("CREATE YOUR TIME TABLE")
    n=int(input("Enter the no of sections in your time table : "))
    for i in range(n):
        print("Enter the time : ",end=" ")
        t=str(input())
        print(" Enter the message to be spoken : ",end=" ")
        tm[t]=str(input())
    while True:
        curtime=time.localtime()
        presenttime=str(curtime.tm_hour)+":"+str(curtime.tm_min)+":"+str(curtime.tm_sec)
        if presenttime in tm.keys():
            for i in range(5):
                speak=pyttsx3.init()
                voices=speak.getProperty('voices')
                speak.setProperty('voice',voices[1].id)
                speak.setProperty('rate',140)
                speak.say(tm[presenttime])
                speak.runAndWait()
        else:
            time.sleep(1)
else:
    print("choosen wrong number..!")
