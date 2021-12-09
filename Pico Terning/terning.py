from machine import Pin, Timer
import math
import random
import time
import lowpower


br = Pin(0, Pin.OUT)
bl = Pin(1, Pin.OUT)
mr = Pin(2, Pin.OUT)
ml = Pin(3, Pin.OUT)
tr = Pin(4, Pin.OUT)
tl = Pin(5, Pin.OUT)
mm = Pin(6, Pin.OUT)
tm = Pin(7, Pin.OUT)
bm = Pin(8, Pin.OUT)

timer = Timer()

pins = [[tl, tm, tr], [ml, mm, mr], [bl, bm, br]]
values = [ [[0,0,0],[0,1,0],[0,0,0]], [[0,0,1],[0,0,0],[1,0,0]], [[1,0,0],[0,1,0],[0,0,1]], [[1,0,1],[0,0,0],[1,0,1]], [[1,0,1],[0,1,0],[1,0,1]], [[1,0,1],[1,0,1],[1,0,1]] ], \
         [ [[0,0,0],[0,1,0],[0,0,0]], [[1,0,0],[0,0,0],[0,0,1]], [[0,0,1],[0,1,0],[1,0,0]], [[1,0,1],[0,0,0],[1,0,1]], [[1,0,1],[0,1,0],[1,0,1]], [[1,1,1],[0,0,0],[1,1,1]] ]
   


def trigger():
    global rolling
    rolling = rolling + 1

rolling = 0


def throw():
    counter = random.randint(0, 5)
    return counter
   
def show(result):   
    orientation = random.randint(0, 1)
    for row in [0, 1, 2]:
        for column in [0, 1, 2]:
            pins[row][column].value(values[orientation][result][row][column])

def off():
    for row in [0, 1, 2]:
        for column in [0, 1, 2]:
           pins[row][column].value(0)        

def roll(numRolls):
    result = 0
    print("Roll now called: ", numRolls)
    for rolls in range(numRolls, 1, -1):
        result = throw()
        time.sleep(1/rolls)
        off()
        time.sleep(0.1)
        show(result)
    time.sleep(5)    
        


random.seed()

#timer.init(freq=0.1, mode=Timer.PERIODIC, callback=roll)


shaking = Pin(10, Pin.IN, Pin.PULL_UP)                 # create input pin for a triggering
shaking.irq(lambda t: trigger())

global rollcount
rollcount = 0

while True:
    if (rolling > 0):
        rollcount = rollcount + 5
        rolling = 0
        time.sleep(0.1)
        continue   
    print(shaking.value())
    if (rollcount > 0):
        roll(rollcount)
        rollcount = 0
        rolling = 0
    else:
      off()
      print("Entering Low Power Mode")
      lowpower.dormant_until_pin(10)
      # while (rolling == 0):
      #    time.sleep(0.1)

 



