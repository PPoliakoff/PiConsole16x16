from PiConsole16x16 import *
import time
console=PiConsole16x16()
perdu=False
px=8
py=8
vx=0
vy=0
snake=[[px,py]]
longueur=55
while not perdu:
    jx=console.joyX()
    jy=console.joyY()
    if abs(jx)>abs(jy):
        vy=0
        vx=1 if jx>0 else -1
    elif abs(jy)>abs(jx):
        vx=0
        vy=1 if jy>0 else -1
    px=(px+vx)%16
    py=(py+vy)%16
    if (vx+vy)!=0 and console.getPixel(px,py)==1:
        perdu=True
    console.setPixel(px,py,1)
    if (vx+vy)!=0:
        snake.append([px,py])
    if len(snake)>longueur:
        console.setPixel(snake[0][0],snake[0][1],0)
        snake.pop(0)
        
    console.refresh()
    time.sleep(0.1)
