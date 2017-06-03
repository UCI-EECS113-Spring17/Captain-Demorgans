
class Bottle:
  
  __slots__ = ["bottleNum","bottleName", "bottleSize", "sleepConstant"]
  
  def __init__(self, index, name, size):
    self.bottleNum = index
    self.bottleName = name
    self.bottleSize = size
    self.sleepConstant = 1
    
  def getSleepTime(liquidAmount):
    return sleepConstant*liquidAmount
