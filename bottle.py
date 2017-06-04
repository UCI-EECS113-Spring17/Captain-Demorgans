
class Bottle:
  
  __slots__ = ["bottleNum","bottleName", "bottleSize", "bottleAmount", "sleepConstant"]
  
  def __init__(self, index, name, size, sleepK):
    self.bottleNum = index
    self.bottleName = name
    self.bottleSize = size
    self.bottleAmount = size
    self.sleepConstant = sleepK
    
  def getSleepTime(liquidAmount):
    return sleepConstant*liquidAmount
