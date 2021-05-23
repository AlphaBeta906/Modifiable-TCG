import sys
import os

__version__ = "V1.1.3"
programs = ["main.py", "player.py", "card.py", "update.py"]

class Update:
  
  def __init__(self):
    try:
      import requests
    except ModuleNotFoundError:
      print('Please down requests for the starting of the update code, please do so by using "python -m pip install requests" or alternatively "pip install requests"')
      sys.exit()
      
    x = requests.get("https://raw.githubusercontent.com/AlphaBeta906/Modifiable-TCG/main/src/update.py")

    with open('update.py', 'r') as f:
        data = f.read()
        
    if x.text.splitlines()[2] != f:
      newVersion = x.text.splitlines()[2].replace('__version__ = ', '').strip('\"')
      print(f"Do you want to update the souce code, to Version {newVersion}? (y/n)\nNOTE: DATABASES WONT BE CHANGED")
      desision = input("> ")

      if desision == "y":

        for code in programs:
          x = requests.get("https://raw.githubusercontent.com/AlphaBeta906/Modifiable-TCG/main/src/main.py")
          open("main.py", "w").write(x)
          file_size = os.getsize(x)
          print (f"Sucessfully imported: {code} {newVersion} ({file_size})

        print ("Version {newVersion} is now imported\nPLEASE CHECK GITHUB REPO FOR NEW FILES TO DOWNLOAD")
      else:
        print ("Update Cancelled. NOTE: ADVANCED CONTENT OR BUG FIXES MIGHT APPEAR IN THE UPDATES")
