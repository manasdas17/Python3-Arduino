import os
import sys
cwd=os.getcwd()
(setpath,Examples)=os.path.split(cwd)
#print setpath
sys.path.append(setpath)

from Arduino.Arduino import Arduino
from time import sleep

class LED_ON_OFF:
    def __init__(self,baudrate):
        self.baudrate=baudrate
        self.setup()
        self.run()  
        self.exit()

    def setup(self):
            self.obj_arduino = Arduino()
            self.port = self.obj_arduino.locateport()
            self.obj_arduino.open_serial(1, self.port,self.baudrate)

    def run(self):
        self.blue=9
        self.obj_arduino.cmd_digital_out(1,self.blue,1)
        sleep(2)
        self.obj_arduino.cmd_digital_out(1,self.blue,0)
        sleep(2)

    def exit(self):
        self.obj_arduino.close_serial()

def main():
    obj_led=LED_ON_OFF(115200)

if __name__== '__main__':
    main()
