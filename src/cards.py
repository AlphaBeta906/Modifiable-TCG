class Card:
  def __init__(self, name, description, atk:int, hp:int, items_active=[]):
    self.name = name
    self.description = description

    item_boosts = [[], []]
    for item in items_active:
      item_boosts[0].append(item.atk_diff)
      item_boosts[1].append(item.hp_diff)

    self.atk = atk + sum(item_boosts[0])
    self.hp = hp + sum(item_boosts[1])
    
  def showCardData(self):
    print (f'\n{self.name}:\n\tDESCRIPTION: "{self.description}" \n\tCURRENT ATK: {self.atk}\n\tCURRENT HP: {self.atk}')
    
class Item:
  def __init__(self, name, description, atk_diff:int, hp_diff:int):
    self.name = name
    self.description = description
    self.atk_diff = atk_diff
    self.hp_diff = hp_diff

  def showCardData(self):
    print (f'\n{self.name}:\n\tDESCRIPTION: "{self.description}" \n\tCURRENT ATK: {self.atk_diff}\n\tCURRENT HP: {self.atk_diff}')
