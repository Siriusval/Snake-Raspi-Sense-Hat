import random
from Snake import Position

class Matrix :
  def __init__(self):
    self.freePos = []

  def createPositiontable(self):
    for i in range(8) :
      for j in range(8):
        self.freePos.append(Position(i,j))
        
  def removePos(self, toRemovePos):
    for pos in self.freePos:
        if pos == toRemovePos:
          self.freePos.remove(toRemovePos)
  
  def addPos(self, toAddPos):
    for pos in self.freePos:
        if pos == toAddPos:
          return
        
    self.freePos.append(toAddPos)    
  
  def getRandomPos(self):
    return self.freePos[random.randint(0,len(self.freePos)-1)]
        