from drink import Drink
from enum import Enum

# Define Drink States
class State(Enum):
	ORDER = 1
	PREPARE = 2
	DISPENSE = 3
	PICKUP = 4

# Load drinks

# Declare Drink State	
machineState = State(1);

# distance sensor
# force sensor
# valve pins for transistors
# drink levels
# buttons / input 
# LCD

def main():
	while(true):
		if(machineState = State.ORDER):
			# display drinks on LCD
			# display drink levels
			# get drink order
			# save order and get instructions on how to make drink
			pass
		elif(machineState = State.PREPARE):
			# prompt user to place cup	
			# make sure all necessary sensors are no longer active
			pass
		elif(machineState = State.DISPENSE):
			# start pouring drink and open/close necessary valves
			pass
		elif(machineState = State.PICKUP):
			# prompt user that drink is ready for pickup
			pass
		
if __name__ == "__main__":
    main()
