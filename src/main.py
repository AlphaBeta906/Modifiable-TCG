# The code you can modify.

# Import all the classes (dont change)
from cards import *
from player import *
from update import *
from random import choices

Update()

# Card Dictionary (edit here!)
cards = [Card("AlphaBeta", "AlphaBeta is a GOD, yeah right a GOD, BOW DOWN TO HIM.", 1000, 1000),
  Card("Underdog", "Underdog is a monster/GOD hybrid.", 180, 70),
  Item("EPIC GAMER!!!1111", "ok", 100, 100)]
  
def main():
  player = Player(choices(cards, k=5))
  print("Player deck:")
  for x in player.cards:
    x.showCardData()
    
if __name__ == "__main__":
  main()
