# --- IMPORT ---
import sense_hat
import time

from Fruit import Fruit
from Snake import Snake
from Timer import Timer
from Matrix import Matrix

# --- GLOBAL ---
clearColor = (0,0,0)
sense = sense_hat.SenseHat()
fruit = Fruit()
snake = Snake(2,4)
timer = Timer()
matrix = Matrix()

running = True

# --- FUNCTIONS ---

  
def init():
  matrix.createPositiontable()
  matrix.removePos(snake.pos[0])
  fruit.changePosition(matrix)
  
def checkIfLoose():
  if snake.pos[0].x < 0 or snake.pos[0].x > 7 or snake.pos[0].y < 0 or snake.pos[0].y > 7:
    running = False
    

def display():
  
  if running :
    sense.clear(clearColor)
  
    sense.set_pixel(fruit.pos.x, fruit.pos.y,fruit.rgb)
    
    for pos in snake.pos:
      sense.set_pixel(pos.x, pos.y, snake.rgb)
  
  else:
      sense.clear(255,0,0)


def updateLogic():
    
    events = sense.stick.get_events()
    if ( len(events) == 0):
      snake.moveAuto(matrix)
    else:
      for event in events:
          if (event.action == "pressed"):
              snake.move(event.direction, matrix)
    
    
    checkIfLoose()
    
    if running :
      snake.checkIfFruit(fruit, matrix)


# --- MAIN ---
def main() :
  init()
  
  while running:
    
    timer.update()

    if (timer.eventCount >= 1): #1sec elapsed

      updateLogic()
      display()
      timer.eventCount -=1
  
  
# DO NOT TOUCH
main()
