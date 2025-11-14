from PiConsole16x16 import *
import time
console=PiConsole16x16()

while True:
    x=console.joyX()+7
    y=console.joyY()+7
    
    console.clear()
    for i in range(16):
        console.setPixel(x,i,1)
        console.setPixel(i,y,1)
    console.refresh()
    time.sleep(0.25)