from time import sleep
from pynq.iop import Arduino_Analog

forcePin = 0
forceSensor = Arduino_Analog(3, [forcePin])


while(True):
    forceReading = forceSensor.read()
    print(forceReading)
    sleep(1) 
