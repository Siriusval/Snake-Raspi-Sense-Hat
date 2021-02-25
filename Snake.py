from Fruit import Fruit
from Position import Position

class Position:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
      
    
class Snake:
  def __init__(self, posX, posY):
    self.pos = [Position(posX,posY)]
    self.rgb = (0,255,0)
    self.len = 1
    self.lastDirection = ""
  
  def checkIfFruit(self, fruit,matrix):
    if self.pos[0] == fruit.pos:
      self.len +=1;
      self.pos.append(fruit.pos)
      matrix.removePos(fruit.pos)
      fruit.changePosition(matrix)
      
    
  def getLastPosition(self):
    return self.pos[self.len-1]
    
  def move(self, direction, matrix):
    self.lastDirection = direction
    
    if (direction != ""):
      lastPos = self.getLastPosition()
      newPosition = Position(lastPos.x,lastPos.y)
      if (direction == "up") :
        newPosition.y -= 1
        self.pos.append(newPosition)
      elif (direction == "down") :
        newPosition.y += 1
        self.pos.append(newPosition)
      elif (direction == "left") :
        newPosition.x -= 1
        self.pos.append(newPosition)
      elif (direction == "right") :
        newPosition.x += 1
        self.pos.append(newPosition)
      
      matrix.removePos(newPosition)
      oldPosition = self.pos[0]
      matrix.addPos(oldPosition)
      
      self.pos.pop(0)
  
  def moveAuto(self, matrix):
    self.move(self.lastDirection, matrix)
    
    

