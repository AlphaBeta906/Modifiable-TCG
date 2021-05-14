import requests

__version__ = "V1.1.2"

class Update:
  
  def __init__(self):
    x = requests.get("https://raw.githubusercontent.com/AlphaBeta906/Modifiable-TCG/main/src/update.py")

    if x[3] != open("update.py", "r"):
      print(f"Do you want to update the souce code, Version {x[3].replace('__version__ = ', '')}? (y/n)/nNOTE: DATABASES WONT BE CHANGED")
      desision = input("> ")

      if desision == "y":
        x = requests.get("https://raw.githubusercontent.com/AlphaBeta906/Modifiable-TCG/main/src/main.py")
        open("main.py", "r").write(x)

        x = requests.get("https://raw.githubusercontent.com/AlphaBeta906/Modifiable-TCG/main/src/card.py")
        open("card.py", "r").write(x)

        x = requests.get("https://raw.githubusercontent.com/AlphaBeta906/Modifiable-TCG/main/src/player.py")
        open("player.py", "r").write(x)
      else:
        print ("Update Cancelled. NOTE: ADVANCED CONTENT OR BUG FIXES MIGHT APPEAR IN THE UPDATES")
