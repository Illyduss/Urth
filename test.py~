import time
import sys

counter = 0

def tick():
    time_start = time.time()
    seconds = 0
    counter = 0

    while True:
        time.sleep(1)
        seconds = int(time.time() - time_start) - counter * 5
        if seconds >= 5:
            counter += 1
            seconds = 0
    return counter

tick()
