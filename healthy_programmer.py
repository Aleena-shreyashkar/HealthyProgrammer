#healthy programmer
"""
water reminder after every 26 min
exercise reminder after every 45 min
eyes relief reminder after every 30 min
"""
from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while(True):
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':
    init_water = time()
    init_exercise = time()
    init_eyes = time()
    watersecs = 5
    exsecs = 10
    eyessecs = 15
    while True:
        if init_water>watersecs:
            print("time to drink water. Enter 'drank' to stop the alarm")
            musiconloop("water.mp3","drank")
            init_water = time()
            log_now("drank water at ")
        elif init_exercise>exsecs:
            print("time to exercise. Enter 'done' to stop the alarm")
            musiconloop("exercise.mp3","done")
            init_exercise = time()
            log_now("done exercise at ")
        elif init_eyes>eyessecs:
            print("time for eyes relief. Enter 'yes' to stop the alarm")
            musiconloop("eyes.mp3","yes")
            init_water = time()
            log_now("eyes relieved at ")
