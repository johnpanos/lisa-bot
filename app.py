import time
import subprocess
from contacts import getName
from database import Database
import config
from chat import Chat

from pathlib import Path
HOME = str(Path.home())

prevRowId = 0

class Message:
  def __init__(self, rowid=-1, text=""):
    self._rowid = rowid
    self._text = text

class Command:
  def __init__(self, command, helpText):
    self._command = command
    self._help = helpText

  def __call__(self, messageArr, recipient):
    print("Not Implemented")

  def getCommand(self):
    return self._command

  def getHelp(self):
    return self._help

db = Database(HOME + "/Library/Messages/chat.db")

class Help(Command):
  def __init__(self):
    super().__init__('help', "Help will print out this message!")

  def __call__(self, messageArr, recipient):
    message = "HELP\n"
    for cmd in commands.items():
      message += "{0}{1}: {2}".format(config.PREFIX, cmd[1].getCommand(), cmd[1].getHelp())
    sendMessage(message, recipient)

class Shuttle(Command):
  def __init__(self, command, helpText):
    super().__init__("shuttle", "Get current shuttle times!")
  
  def __call__(self, messageArr, recipient):
    sendMessage("Not done :(", recipient)

commands = {
  "help": Help()
}

def handleCommand(message, recipient, name):
  if message[0] == "!":
    print("Command found")
    commandList = message.split(" ")
    command = commandList[0][1:].lower()
    print("Command", command)
    # print("Parameter", commandList[1])
    if command in commands:
      commands[command](commandList, recipient)

def sendMessage(message, recipient):
  subprocess.call(["osascript", "send.scpt", message, recipient])

while True:
  newId = db.getLastRowId()
  if newId != prevRowId:
    print("different")
    message = db.getMessageForRowId(newId)
    chat = Chat(message[2], message[1])
    print(message)
    # print("{0}: {1}".format(message[0], getName(message[1])))
    # handleCommand(message[0], message[1], getName(message[1]))
    print(chat)
    chat.sendMessage("Test")
    prevRowId = newId
  time.sleep(1)
