from PiConsole16x16 import *
import time
import random
console=PiConsole16x16()
perdu=False
px=8
left=[3]*16
right=[13]*16
w=10
distance=0
while not perdu:
    jx=console.joyX()
    if jx>1 and px <14:
        px+=1
    elif jx<-1 and px>1:
        px-=1
    l=left[15]+random.randint(-1,1)
    if l<0:
        l=0
    if l+w>15:
        l-=1
    left.append(l)
    left.pop(0)
    right.append(l+w)
    right.pop(0)
    distance+=1
    if distance%50==0:
        w-=1
    if px+1>=right[0] or px<=left[0]:
        perdu=True
    console.clear()
    for i in range(16):
        console.setPixel(left[i],15-i,1)
        console.setPixel(right[i],15-i,1)
    for i in range (14,16):
        console.setPixel(px,i,1)
        console.setPixel(px+1,i,1)
    console.refresh()
    time.sleep(0.1)
