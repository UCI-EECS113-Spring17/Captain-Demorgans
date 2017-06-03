
class Bottle:
  
  __slots__ = ["bottleNum","bottleName", "bottleSize"]
  
  def __init__(self, index, name, size):
    self.bottleNum = index
    self.bottleName = name
    self.bottleSize = size
