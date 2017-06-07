
# coding: utf-8

# In[4]:

from time import sleep
from pynq.iop import *
from bottle import *
from drinks import * 
from enum import Enum

# Name of Drink file to load from
#drink_file = sys.argv[1]
drinkFile = "drinkList.txt"

# Define Drink States
class State(Enum):
    ORDER = 1
    PREPARE = 2
    DISPENSE = 3
    PICKUP = 4

# Load drinks
ingredients = [] 
drinks = []
#Average flow-rate of each bottle Oz/s
drinkConstant = [0.34, 0.343, 0.348, 0.365]
bottleSize = [16.9 for i in range(0,4)]
#maps ingredient name to bottle
bottleDictionary = dict()
# Declare Drink State
machineState = State(1)
currDrink = None
basePin = 0
forceSensor = Arduino_Analog(3, [forcePin])
index = 0
timeOn = 1
timeOff = 1

# Load text file into different objects
def loadFile(fname):
    global ingredients, drinks
    count = 0
    with open(fname, 'r') as drinkFile:
        for line in drinkFile.readlines():
            lines = line.rstrip()
            #change to pointer for some reason
            lines.rstrip()
            if count == 0:
                #all ingredients on the machine
                ingredients = lines.split('\t')
                declareBottles(ingredients)
            else:
                #get drink names
                args = lines.split('\t')
                #add ingredients to the drink
                if line[0] != '\t':
                    drinks.append(Drink(args[0]))
                else: 
                    del args[0]
                    drinks[len(drinks)-1].addIngredient(args[0], args[1])
                    #print(args)
            count += 1
            
#load bottles from text file
# bottle name -> bottle
def declareBottles(ingredients):
    global drinkConstant, bottleSize
    index = 0
    for i in ingredients:
        bottleDictionary[i] = Bottle(index, i, bottleSize[index], drinkConstant[index])
        index += 1
        
def makeDrink():
    # iterate through the ingredients
    # go one ingredient at a time and also the amount
    # locate the bottle index (which vale to turn on)
    global currDrink, machineState, bottleDictionary
    for bottleName in currDrink.drinkList:
        # get the bottle object
        bottle = bottleDictionary[bottleName]
        # get the amount to dispense
        amount = float(currDrink.drinkList[bottleName])
        k = float(bottle.sleepConstant)
        sleepTime = amount/k
        print(sleepTime)
        bottleIndex = bottle.bottleNum
        bottle.dispense(amount)
        #turn on the valve
        valve[bottleIndex].write(1)
        #sleep certian num of seconds
        sleep(sleepTime)
        #turn off the valve
        valve[bottleIndex].write(0)
        sleep(0.1)
    machineState = State.PICKUP

loadFile(drinkFile)
print(machineState)
while(1):
    if(machineState == State.ORDER):
        print("Order a Drink.")
        sleep(1)
        currDrink = drinks[7]
        print(currDrink.drinkName)
        machineState = State.PREPARE
    elif(machineState == State.PREPARE):
        # prompt user to place cup	
        # make sure all necessary sensors are no longer active
        print("Ready to make drink")
        sleep(1)
        machineState = State.DISPENSE
    elif(machineState == State.DISPENSE):
        # start pouring drink and open/close necessary valves
        print("Pouring drink")
        makeDrink()
    elif(machineState == State.PICKUP):
        # prompt user that drink is ready for pickup
        print("Drink is ready for pickup")
        break
print("Program has finished")
for b in bottleDictionary:
    print(bottleDictionary[b].getInfo())
for d in drinks:
    print(d.drinkName)

