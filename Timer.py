import time

class Timer:
  def __init__(self):
    self.elapsed = 0.0
    self.delay = 1.0
    self.lastRegisteredTime = time.time()
    self.eventCount = 0
    
  def update(self):
    currentTime = time.time()
    self.elapsed = currentTime - self.lastRegisteredTime
    
    if(self.elapsed >= 1):
      self.lastRegisteredTime = currentTime
      self.eventCount += 1
      
      
    
    