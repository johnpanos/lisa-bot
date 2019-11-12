import time
import subprocess
from contacts import getName
from database import Database

from pathlib import Path
HOME = str(Path.home())

prevRowId = 0

class Message:
  def __init__(self, rowid=-1, text=""):
    self._rowid = rowid
    self._text = text

db = Database(HOME + "Library/Messages/chat.db")

PREFIX = "!"
def manageShit(message, recipient, name):
  if message[0] == "!":
    print("Command found")
    commandList = message.split(" ")
    command = commandList[0][1:]
    print("Command", command)
    # print("Parameter", commandList[1])
    sendMessage(message, recipient)

def sendMessage(message, recipient):
  subprocess.call(["osascript", "send.scpt", message, recipient])

while True:
  newId = db.getLastRowId()
  if newId != prevRowId:
    print("different")
    message = db.getMessageForRowId(newId)
    print(message)
    print("{0}: {1}".format(message[0], getName(message[1])))
    manageShit(message[0], message[1], getName(message[1]))
    prevRowId = newId
  time.sleep(1)