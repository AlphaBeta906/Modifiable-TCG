class Card:
  def __init__(self, name, description, atk, hp):
    self.name = name
    self.description = description
    self.atk = atk
    self.hp = hp
    
  def showCardData(self):
    print(f'{self.name}:\nDescription: {self.description}\nATK: {self.atk}\nHP: {self.hp}')
    
  def showSpecificData(self, var):
    return getattr("self", var)
