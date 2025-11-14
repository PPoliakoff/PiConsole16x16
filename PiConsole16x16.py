from machine import Pin,SPI,ADC
class PiConsole16x16:
    def __init__(self):
        self.spi=SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
        self.cs=Pin(5, Pin.OUT)
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
        retval=-((ADC(28).read_u16()-29000)//4096)
        if retval<-7:
            retval=-7
        elif retval>8:
            retval=8
        return retval 
    
    def joyY(self):
        retval= (ADC(27).read_u16()-29000)//4096
        if retval<-7:
            retval=-7
        elif retval>8:
            retval=8
        return retval 
