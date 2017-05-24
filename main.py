#!/usr/bin/env python
from drinks import Drink
from enum import Enum
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
# Declare Drink State	
machineState = State(1);

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
