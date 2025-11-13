from machine import Pin,SPI,ADC
from utime import sleep
import random

class LED_display16x16:
    def __init__(self,spi,cs):
    
        self.spi=spi
        self.cs=cs
        self.broadcast(0x0C, 0) #shudown on
        self.broadcast(0x0A, 2) #brightness
        self.broadcast(0x0F, 0) #demo off
        self.broadcast(0x0B, 7) #scan lines
        self.broadcast(0x09, 0) #decode off
        self.broadcast(0x0C, 1) #shudown off
        self.mat=bytearray(32);
        self.clear()
        self.refresh()
     
    def clear(self):
        for i in range(32):
            self.mat[i]=0
     
    def broadcast(self,command,value):
        self.cs.value(0)
        for i in range(4):
            self.spi.write(bytearray([command, value]))
        self.cs.value(1)

    def refresh(self):
        for j in range(8):
            self.cs.value(0)
            for i in range(4):
                self.spi.write(bytearray([j+1, self.mat[j*4+3-i]]))
            self.cs.value(1)
             
           
    def setPixel(self,x,y,c):
        x=15-x
        if y<8:
            idx=2+4*y
        else:
            idx=4*(y-8)
        if x>7:
            idx+=+1
        if c==0:
            self.mat[idx]&=~(1<<(x&0x07))
        else:
            self.mat[idx]|=1<<(x&0x07)

    def getPixel(self,x,y):
        x=15-x
        if y<8:
            idx=2+4*y
        else:
            idx=4*(y-8)
        if x>7:
            idx+=+1
        return 0 if self.mat[idx]&(1<<(x&0x07))==0 else 1


    def joyX(self):
        return -(ADC(28).read_u16()//4096-8)
    
    def joyY(self):
        return ADC(27).read_u16()//4096-8



spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
cs = Pin(5, Pin.OUT)
display = LED_display16x16(spi, cs)

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
    sleep(0.1)
    
display.refresh()


