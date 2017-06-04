#!/usr/bin/env python
from drinks import Drink
from bottle import Bottle
from enum import Enum
#from pynq.iop import *
import sys

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
drinkConstant = [0.24, 0.243, 0.348, 0.25]
bottleSize = [16.9 for i in range(0,4)]
#maps ingredient name to bottle
bottleDictionary = dict()
# Declare Drink State	
machineState = State(1)
currDrink = None
# distance sensor
# force sensor
# valve pins for transistors
# drink levels
# buttons / input 
# LCD

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
		
def prepareDrink():
	# iterate through the ingredients
	# go one ingredient at a time and also the amount
	# locate the bottle index (which vale to turn on)
	global currDrink, machineState, bottleDictionary
	for bottleName in currDrink.drinkList:
		# get the bottle object
		bottle = bottleDictionay[bottleName]
		# get the amount to dispense
		amount = currDrink.drinkList[bottleName]
		sleepTime = bottle.getSleepTime(amount)
		#turn on the valve
		#sleep certian num of seconds
		#turn off the valve
	machineState = State.PICKUP
	
def checkForceSensor():
	# check the force sensor 
	# determine the threshold to trigger dispense state
	pass
		
def main():
	loadFile(drinkFile);
	while(True):
		if(machineState == State.ORDER):
			# display drinks on LCD
			# display drink levels
			# get drink order
			# save order and get instructions on how to make drink
			pass
		elif(machineState == State.PREPARE):
			# prompt user to place cup	
			# make sure all necessary sensors are no longer active
			pass
		elif(machineState == State.DISPENSE):
			# start pouring drink and open/close necessary valves
			pass
		elif(machineState == State.PICKUP):
			# prompt user that drink is ready for pickup
			pass
		break

	print("\nIngredients:")
	for i in ingredients:
		pass
		print(i)

	print("\nDrinks:")
	for d in drinks:
		pass
		print(d.getDrinkName())
		print(d.getIngredients())
		
if __name__ == "__main__":
    main()
