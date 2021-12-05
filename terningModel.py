
import math
from threading import Timer


currentVelX=0.1
currentVelY=0
currentPositionLa = 0
currentPositionLo = 0




def nextMove():
    global currentPositionLa, currentPositionLo
    print("Calling nextMove()")
    tim = Timer( 1, nextMove )
    tim.start()
    newX = math.sin(currentPositionLa) * math.cos(currentPositionLo) + currentVelX
    newY = math.sin(currentPositionLa) * math.sin(currentPositionLo) + currentVelY
    currentPositionLa = math.atan(newY/newx)
    currentPositionLo =  
       (math.cos(currentPositionLa) * math.sin(currentPositionLa) + currentVelX)
    currentPositionLa =  math.fmod(math.pi*2, currentPositionLa + currentVelocity * math.cos(currentDir) )
    currentPositionLo =  math.fmod( math.pi*2, currentPositionLo + currentVelocity * math.sin(currentDir) )
    print("Curr: ", currentPositionLa, currentPositionLo)



nextMove()