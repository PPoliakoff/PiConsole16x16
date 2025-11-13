from PiConsole16x16 import *
import time
import random
display=PiConsole16x16()


x=random.randrange(0,16)
y=11
dx=1
dy=-1
px=8
display.setPixel(px-1,15,1)
display.setPixel(px,15,1)
display.setPixel(px+1,15,1)
for i in range(16):
    display.setPixel(i,3,1)
    display.setPixel(i,4,1)
    display.setPixel(i,5,1)
gameover=False
while not gameover:
    px+=display.joyX()//4
    if px>14:
             px=14
    if px<1:
         px=1
    for i in range(16):
        if i-px <2 and i-px>-2:
            display.setPixel(i,15,1)
        else:
            display.setPixel(i,15,0)
            
    display.setPixel(x,y,0)    
    x+=dx
    y+=dy
    if x<=0:
        x=0
        dx=1
    elif x>=15:
        x=15
        dx=-1
    if y<6 and display.getPixel(x,y)==1:
        dy=-dy
    display.setPixel(x,y,1)

    if y==0:
        dy=1
    elif y==14:
        if x+dx==px:
            dx=0
            dy=-1
        elif x+dx==px-1:
            dx=-1
            if x==0:
                x=1
            dy=-1
        elif x+dx==px+1:
            dx=1
            if x==15:
                x=14
            dy=-1
    elif y==15:
            gameover=True


    display.refresh()
    time.sleep(0.1)
    
display.refresh()


