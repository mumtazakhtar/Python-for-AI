import time
from playsound import playsound

def countdown_timer(seconds):
    while seconds>0:
        mins=int(seconds/60)
        secs=int(seconds%60)
        timer=f'{mins}:{secs}'
        print(timer)
        seconds -= 1 #seconds=seconds-1
    print("TIME UP!!")

# input time in seconds
seconds = input("Enter the time in seconds: ")
# call the function
countdown_timer(int(seconds))
# Adding sound to the timer code
time.sleep(int(seconds))
playsound(r"C:\Users\akhta\OneDrive\Desktop\python\ding-101492.mp3", True)
