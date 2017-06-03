
class Bottle:
  
  __slots__ = ["bottleNum","bottleName", "bottleSize", "bottleAmount", "sleepConstant"]
  
  def __init__(self, index, name, size):
    self.bottleNum = index
    self.bottleName = name
    self.bottleSize = size
    self.bottleAmount = size
    self.sleepConstant = 1
    
  def getSleepTime(liquidAmount):
    return sleepConstant*liquidAmount
