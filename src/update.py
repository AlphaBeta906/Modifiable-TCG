import requests

__version__ = "V1.1.2"
programs = ["main.py", "player.py", "card.py", "update.py"]

class Update:
  
  def __init__(self): 
    x = requests.get("https://raw.githubusercontent.com/AlphaBeta906/Modifiable-TCG/main/src/update.py")
        
    if x.text.splitlines()[2] != __version__:
      newVersion = x.text.splitlines()[2].replace('__version__ = ', '').strip('\"')
      print(f"Do you want to update the souce code, to Version {newVersion}? (y/n)\nNOTE: DATABASES WONT BE CHANGED")
      desision = input("> ")

      if desision == "y":

        for code in programs:
          x = requests.get("https://raw.githubusercontent.com/AlphaBeta906/Modifiable-TCG/main/src/main.py")
          open("main.py", "w").write(x.text)
          print (f"Sucessfully imported: {code} {newVersion}")

        print ("Version {newVersion} is now imported\nPLEASE CHECK GITHUB REPO FOR NEW FILES TO DOWNLOAD")
      else:
        print ("Update Cancelled. NOTE: ADVANCED CONTENT OR BUG FIXES MIGHT APPEAR IN THE UPDATES")
