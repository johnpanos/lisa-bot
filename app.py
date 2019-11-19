import os
import time
import subprocess
from database import Database
import config
from imessage import Chat, Message, Recipient

from pathlib import Path
HOME = str(Path.home())

db = Database(HOME + "/Library/Messages/chat.db")
prevRowId = db.getLastRowId()

class Command:
  def __init__(self, command, helpText):
    self._command = command
    self._help = helpText

  def __call__(self, message, messageArr):
    print("Not Implemented")

  def getCommand(self):
    return self._command

  def getHelp(self):
    return self._help

class Help(Command):
  def __init__(self):
    super().__init__('help', "Help will print out this message!")

  def __call__(self, message, messageArr):
    output = "HELP"
    for cmd in commands.items():
      output += "\n\n{0}{1}: {2}".format(config.PREFIX, cmd[1].getCommand(), cmd[1].getHelp())
    message.getChat().sendMessage(output)

class Shuttle(Command):
  def __init__(self):
    super().__init__("shuttle", "Get current shuttle times!")
  
  def __call__(self, message, messageArr):
    message.getChat().sendMessage("Not done :(")

class Name(Command):
  def __init__(self):
    super().__init__("name", "Print out your name associated with your number!")

  def __call__(self, message, messageArr):
    message.getChat().sendMessage("Your name is: {0}".format(message.getChat().getRecipient().getName()))

class WordStatistic(Command):
  def __init__(self):
    super().__init__("wordstat", "Pass this command a word, and it'll send a graph of who stays the word the most in decreasing order!")
  
  def __call__(self, message, messageArr):
    chat = message.getChat()
    print(chat)
    if not chat.isGroup():
      chat.sendMessage("This command only works with group chats!")
      return
    # chat.sendImage(os.getcwd() + "/gb.jpg")

    chat.sendMessage("Not finished.")

class Gayle(Command):
  def __init__(self):
    super().__init__("gayle", "mmmmmmmmm gayle beebe oh yeah mhm")

  def __call__(self, message, messageArr):
    chat = message.getChat()
    chat.sendImage(os.getcwd() + "/gb.jpg")

  

commands = {
  "help": Help(),
  "shuttle": Shuttle(),
  "name": Name(),
  "wordstat": WordStatistic(),
  "gayle": Gayle()
}

def handleCommand(message):
  cmd = message.getText()
  if cmd[0] == "!":
    commandList = cmd.split(" ")
    command = commandList[0][1:].lower()
    print("Command:", command)
    # print("Parameter", commandList[1])
    if command in commands:
      commands[command](message, commandList)
    else:
      message.getChat().sendMessage("Unknown Command: {0}".format(command))

while True:
  rows = db.getLastRowId(prevRowId)
  i = 0
  for row in rows:
    prevRowId = row[0]
    messageObject = Message(row[1], Chat(row[3], row[2]))
    handleCommand(messageObject)
  # if newId != prevRowId:
  #   message = db.getMessageForRowId(newId)

  time.sleep(2)
