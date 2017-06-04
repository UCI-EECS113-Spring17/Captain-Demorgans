
class Bottle:
  
  __slots__ = ["bottleNum","bottleName", "bottleSize", "bottleAmount", "sleepConstant"]
  
  def __init__(self, index, name, size, sleepK):
    self.bottleNum = index
    self.bottleName = name
    self.bottleSize = size
    self.bottleAmount = size
    self.sleepConstant = sleepK
    
  def getSleepTime(self, liquidAmount):
    return sleepConstant*liquidAmount

  def getAmount(self):
    return self.bottleAmount
  
  def dispense(self, liquidAmount):
    self.bottAmount -= liquidAmount

  def getInfo(self):
    info = str(self.bottleNum) + ": " + self.bottleName + "\tSize: " + str(self.bottleSize) +"\tAmount: " + str(self.bottleAmount) + "\tZZZ Time:" + str(self.sleepConstant) 
    return info

