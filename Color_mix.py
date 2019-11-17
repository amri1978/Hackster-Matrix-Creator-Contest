from matrix_lite import led
from time import sleep
from math import pi, sin
from random import randint
import matrix_lite_nfc as nfc


everloop = ['black'] * led.length
counter = 0.0
tick = len(everloop) - 1
isChanged = False
nextPosCounterClockWise = 34
nextPosClockWise = 1
debug = False
direction = 0


def gameOver():
    everloop = ['black'] * led.length

    ledAdjust = 0.0
    if len(everloop) == 35:
        ledAdjust = 0.51 # MATRIX Creator
    else:
        ledAdjust = 1.01 # MATRIX Voice

    frequency = 0.375
    counter = 0.0
    tick = len(everloop) - 1
    
    count = 0
    while count < 70:
        # Create rainbow
        for i in range(len(everloop)):
            r = round(max(0, (sin(frequency*counter+(pi/180*240))*155+100)/10))
            g = round(max(0, (sin(frequency*counter+(pi/180*120))*155+100)/10))
            b = round(max(0, (sin(frequency*counter)*155+100)/10))

            counter += ledAdjust

            everloop[i] = {'r':r, 'g':g, 'b':b}

        # Slowly show rainbow
        if tick != 0:
            for i in reversed(range(tick)):
                everloop[i] = {}
            tick -= 1

        led.set(everloop)
        sleep(.035)
        count += 1
        
        
        
def colorPick():
    # Pick a random number representing one of four colors (yellow, blue, red and white) and there is a 1/40 chance to pick a golden ball
    x =  randint(0,40)

    # Return the color matching that random number
    if x <= 10:
        color = 'yellow'
    elif x <= 20:
        color = 'blue'
    elif x <= 30:
        color = 'red'
    elif x <= 39:
        color = 'white'
    else:
        color = 'white' #'darkgoldenrod'
    return color

	
def debugEverloop(): #a debug function to print all the leds color's
    if (not debug):
        return
    message=''
    if direction == 1:
        for i in range(0,35):
            if everloop[i] == 'red':
   	           message += 'Red-'
            elif everloop[i] == 'blue':
               message += 'Blue-'
            elif everloop[i] == 'green':
               message += 'Green-'   
            elif everloop[i] == 'white':
               message += 'White-'
            elif everloop[i] == 'black':
               message += 'Empty-'
            elif everloop[i] == 'orange':
               message += 'Orange-'
            elif everloop[i] == 'purple':
               message += 'Purple-'
            elif everloop[i] == 'darkgoldenrod':
               message += 'Golden-'
            elif everloop[i] == 'yellow':
               message += 'Yellow-'
        print(message + '\n')
        print('NextPosClockwise = ' , nextPosClockWise,'\n')
    elif direction == -1:
        for i in reversed(range(0,35)):
            if everloop[i] == 'red':
   	           message += 'Red-'
            elif everloop[i] == 'blue':
               message += 'Blue-'
            elif everloop[i] == 'green':
               message += 'Green-'   
            elif everloop[i] == 'white':
               message += 'White-'
            elif everloop[i] == 'black':
               message += 'Empty-'
            elif everloop[i] == 'orange':
               message += 'Orange-'
            elif everloop[i] == 'purple':
               message += 'Purple-'
            elif everloop[i] == 'darkgoldenrod':
               message += 'Golden-'
            elif everloop[i] == 'yellow':
               message += 'Yellow-'
        print(message + '\n')
        print('NextPosCounterClockWise = ' , nextPosCounterClockWise,'\n')
		
        
def RecursiveMixClockWise():
    global isChanged, nextPosClockWise, debug
    if not isChanged:
        return
    isChanged = False
    for i in reversed(range (2, nextPosClockWise)):
        if everloop[i-1] == everloop[i]:
            if debug:
                print('Mergin two balles ', i, i-1, '\n')
            everloop[nextPosClockWise] = 'black'
            for j in range (i,nextPosClockWise):
                everloop[j] = everloop[j+1]
            nextPosClockWise -= 1
            debugEverloop()
            isChanged = True
            renderSlow()
            break
    if everloop[2] == 'white':
        if debug:
            print('White Ball ahead')
        for i in range(2,nextPosClockWise):
            everloop[i] = everloop[i+1]
        everloop[nextPosClockWise] = 'black'
        nextPosClockWise -= 1
        debugEverloop()
        isChanged=True
        renderSlow()
    for i in reversed(range(2,nextPosClockWise + 1)):
        if {everloop[i],everloop[i-1]} == {'yellow','blue'}:
            if debug:
                print('Mixing two colors ', i,' and ',i-1, '\n')
            everloop[nextPosClockWise] = 'black'
            everloop[i-1] = 'green'
            for j in range(i,nextPosClockWise):
                everloop[j] = everloop[j+1]
            nextPosClockWise -= 1
            debugEverloop()
            isChanged = True
            renderSlow()
            break
    for i in reversed(range(2,nextPosClockWise + 1)):
        if {everloop[i],everloop[i-1]} == {'red','blue'}:
            if debug:
                print('Mixing two colors ', i,' and ',i-1, '\n')
            everloop[nextPosClockWise] = 'black'
            everloop[i-1] = 'purple'
            for j in range(i,nextPosClockWise):
                everloop[j] = everloop[j+1]
            nextPosClockWise -= 1
            debugEverloop()
            isChanged = True
            renderSlow()
            break
    for i in reversed(range(2,nextPosClockWise + 1)):
        if {everloop[i],everloop[i-1]} == {'red','yellow'}:
            if debug:
                print('Mixing two colors ', i,' and ',i-1, '\n')
            everloop[nextPosClockWise] = 'black'
            everloop[i-1] = 'orange'
            for j in range(i,nextPosClockWise):
                everloop[j] = everloop[j+1]
            nextPosClockWise -= 1
            debugEverloop()
            isChanged = True
            renderSlow()
            break
    RecursiveMixClockWise()



def RecursiveMixCounterClockWise():
    global isChanged, nextPosCounterClockWise, debug
    if not isChanged:
        return
    isChanged = False
    for i in reversed(range (nextPosCounterClockWise + 1,35)):
        if everloop[i] == everloop[i-1]:
            if debug:
                print('Mergin two balles ', i, i-1, '\n')
            everloop[nextPosCounterClockWise] = 'black'
            for j in reversed(range (nextPosCounterClockWise + 1,i+1)):
                everloop[j] = everloop[j-1]
            nextPosCounterClockWise += 1
            debugEverloop()
            isChanged = True
            renderSlow()
            break
    if everloop[33] == 'white':
        if debug:
            print('White Ball ahead')
        for i in reversed(range(nextPosCounterClockWise + 1,34)):
            everloop[i] = everloop[i-1]
        everloop[nextPosCounterClockWise] = 'black'
        nextPosCounterClockWise += 1
        debugEverloop()
        isChanged=True
        renderSlow()
    for i in reversed(range (nextPosCounterClockWise + 1,35)):
        if {everloop[i],everloop[i-1]} == {'yellow','blue'}:
            if debug:
                print('Mixing two colors ', i,' and ',i-1, '\n')
            everloop[nextPosCounterClockWise] = 'black'
            everloop[i] = 'green'
            for j in reversed(range (nextPosCounterClockWise + 1,i)):
                everloop[j] = everloop[j-1]
            nextPosCounterClockWise += 1
            debugEverloop()
            isChanged = True
            renderSlow()
            break
    for i in reversed(range (nextPosCounterClockWise + 1,35)):
        if {everloop[i],everloop[i-1]}=={'red','blue'}:
            if debug:
                print('Mixing two colors ', i,' and ',i-1, '\n')
            everloop[nextPosCounterClockWise] = 'black'
            everloop[i] = 'purple'
            for j in reversed(range (nextPosCounterClockWise+1,i)):
                everloop[j] = everloop[j-1]
            nextPosCounterClockWise += 1
            debugEverloop()
            isChanged = True
            renderSlow()
            break
    for i in reversed(range (nextPosCounterClockWise + 1,35)):
        if {everloop[i],everloop[i-1]} == {'red','yellow'}:
            if debug:
                print('Mixing two colors ', i,' and ',i-1, '\n')
            everloop[nextPosCounterClockWise] = 'black'
            everloop[i] = 'orange'
            for j in reversed(range (nextPosCounterClockWise + 1,i)):
                everloop[j] = everloop[j-1]
            nextPosCounterClockWise += 1
            debugEverloop()
            isChanged = True
            renderSlow()
            break

    RecursiveMixCounterClockWise()

	
def renderSlow():
	led.set(everloop)
	sleep(0.3)
def renderFast():
	led.set(everloop)
	sleep(.15)

	


		
while True:

    everloop[0] = colorPick()
    led0 = everloop[0]
    #make a blink animation of led 0 and wait for a direction
    while direction == 0:
        everloop[0] = led0
        renderFast()
        everloop[0] = 'black'
        renderFast()
        tag = nfc.read.scan({"info": True, "pages": False, "ndef": False,"page": 0})
        if(tag.status == 256):
            if tag.info.UID == '0A24E83C': #Clockwise direction		
                direction = 1
            elif tag.info.UID != '':
                direction = -1
    everloop[0] = led0
    renderSlow()
    if debug:
        print('Next Ball :' , everloop[0])
    debugEverloop()
    foundplace = False
    isChanged = False
    if direction == 1: #clockwise
        if everloop[0] == 'darkgoldenrod': # lucky man
            for i in range (1,nextPosClockWise):
                everloop[i] = 'black'
                renderFast()
            everloop[0] = 'black'			
            nextPosClockWise = 1
		#find place for the new ball
        for i in range(1,nextPosClockWise+1):
            if everloop[i] ==  'black':
                if debug:
                    print('Found empty space n°' , i , ', shifting balls\n')
                for j in reversed(range(1,i+1)):
                    everloop[j] = everloop[j-1]
                everloop[0] = 'black'
                foundplace= True
                nextPosClockWise += 1
                debugEverloop()
                renderSlow()
                break
        if foundplace:
            isChanged = True
            RecursiveMixClockWise()
            direction = 0
        else:
            print('Game Over')
            break
    elif direction == -1: #counterclockwise
        if everloop[0] == 'darkgoldenrod': # lucky man
            for i in  reversed(range(nextPosCounterClockWise,35)):
                everloop[i] = 'black'
                renderFast()
            everloop[0] = 'black'			
            nextPosCounterClockWise = 34
		#find place for the new ball
        for i in reversed(range(nextPosCounterClockWise,35)):
            if everloop[i] ==  'black':
                if debug:
                    print('Found empty space n°' , i , ', shifting balls\n')
                for j in range(i,35):
                    everloop[j] = everloop[ (j+1) % 35]
                everloop[0] = 'black'
                foundplace = True
                nextPosCounterClockWise -= 1
                debugEverloop()
                renderSlow()
                break
        if foundplace:
            isChanged = True
            RecursiveMixCounterClockWise()
            direction = 0
        else:
            print('Game Over')
            gameOver()
            break

