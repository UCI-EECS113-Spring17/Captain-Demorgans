# Organize the Drink Class
# Author: Miguel Escobar
# Date: 5/15/2016
class Drink:
	# drink name, drink list dictionary
	# index (key) is bottle name, liquid amount (value) is in ounces 
	__slots__ = ["drinkName","drinkList"]

	def __init__(self,drinkName):
		self.drinkName = drinkName
		self.drinkList = dict()

	def addIngredient(self,bottleName, liquidAmount):
		self.drinkList[bottleName] = liquidAmount

	def getDrinkName(self):	
		return self.drinkName
	
	def getIngredients(self):
		ingredients = ""
		for k, v in self.drinkList.items():
			ingredients += str(k) + ", " + str(v) + " oz.\n"
		return ingredients 

		
	

	
