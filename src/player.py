class Player:
  def __init__(self, cards=[]):
    self.points = 0
    self.cards = cards
    
  def addPoint(self):
    self.points += 1
