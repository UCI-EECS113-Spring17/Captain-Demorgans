# Organize the Drink Class
# Author: Miguel Escobar
# Date: 5/15/2016
class Drink:
	# drink name, drink list dictionary
	# index (key) is bottle name, liquid amount (value) is in ounces 
	__slots__ = ["drinkName","drinkList"]

	def __init__(drinkName):
		self.drinkName = drinkName
		self.drinkList = dict()

	def addIngredient(bottleName, liquidAmount):
		self.drinkList[bottleName] = liquidAmount

	def getDrinkName():	
		return self.drinkName
	
	def getIngredients():
		ingredients = ""
		for k, v in self.drinkList:
			ingredients += k + ", " + v + " oz.\n"
		return ingredients 

		
	

	
