'''
Fruit Class

Manage the entity builder, attributs
'''

from Position import Position

class Fruit:
  def __init__(self):
    self.pos = Position(0,0)
    self.rgb = (255,0,0)
    
  
  def changePosition(self, matrix):
    self.pos = matrix.getRandomPos()

    
    
  
  


