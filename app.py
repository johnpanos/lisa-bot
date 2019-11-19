import os
import time
import subprocess
from database import Database
import config
from imessage import Chat, Message, Recipient
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
from random import randrange

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
  
  def onlyGroupChat(self):
    return False

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

    if len(messageArr) < 2:
      chat.sendMessage("You must supply a word after the command!")
      return

    word = " ".join(messageArr[1:])
    data = db.getCountForWord(chat, word)
    displayName = chat.getDisplayname()

    try:
      labels = [Recipient(d[1]).getName() + ": " + str(d[0]) for d in data]
      total = sum([d[0] for d in data])
      sizes = [d[0]/total for d in data]

      explode = [0] * len(labels)
      explode[sizes.index(max(sizes))] = 0.05
      explode = tuple(explode)

      fig1, ax1 = plt.subplots()
      ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode)
      ax1.set_title("\"{0}\" in {1}".format(word, displayName))

      centre_circle = plt.Circle((0,0),0.70,fc='white')
      fig = plt.gcf()
      fig.gca().add_artist(centre_circle)

      ax1.axis('equal')  
      plt.tight_layout()
      plt.savefig("tmp/tmpstat.png",bbox_inches='tight',dpi=100)
      chat.sendImage(os.getcwd() + "/tmp/tmpstat.png")
    except:
      chat.sendMessage("Could not find word \"{0}\" in chat!".format(word))

class Gayle(Command):
  def __init__(self):
    super().__init__("gayle", "Shows a random photo of our beloved Beebe")
    path = os.getcwd() + "/beebe"
    self.gaylePhotos = [f for f in listdir(path) if isfile(join(path, f))]

  def __call__(self, message, messageArr):
    chat = message.getChat()
    randomIndex = randrange(len(self.gaylePhotos))
    chat.sendImage(os.getcwd() + "/beebe/" + self.gaylePhotos[randomIndex])

class Debug(Command):
  def __init__(self, command, helpText):
    super().__init__("debug", "Prints debug information to the chat")
  
  def __call__(self, message, messageArr):
    chat = message.getChat()
    output = "Chat: {0}\n".format(chat)

commands = {
  "help": Help(),
  # "shuttle": Shuttle(),
  "name": Name(),
  "wordstat": WordStatistic(),
  "gayle": Gayle(),
  "debug": Debug()
}

def handleCommand(message):
  cmd = message.getText()
  if cmd is None:
    return
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
