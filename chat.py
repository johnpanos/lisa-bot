import subprocess
from contacts import getName

class Recipient:
  def __init__(self, idA, name="Name Not Found"):
    self._id = idA
    self._name = self.getName()

  def getId(self):
    return self._id

  def getName(self):
    return getName(self._id)

  def sendMessage(self, message):
    subprocess.call(["osascript", "send.scpt", message, self._id])

  def __str__(self):
    return "Id: {0}, Name: {1}".format(self._id, self._name)

class Message:
  def __init__(self, message, chat):
    self._message = message
    self._chat = chat

  def getMessage(self):
    return self._message

  def getChat(self):
    return self._chat

  def __str__(self):
    return "Message: {0}\nChat: {1}".format(self._message, str(self._chat))

class Chat:
  def __init__(self, recipient, roomname=None):
    self._roomname =  roomname
    if type(recipient) == str:
      self._recipient = Recipient(recipient)
    else:
      self._recipient = recipient

  def getRecipient(self):
    return self._recipient

  def isGroup(self):
    return self._roomname is not None

  def sendMessage(self, message):
    if self.isGroup():
      subprocess.call(["osascript", "sendgc.scpt", message, "iMessage;+;" + self._roomname])
    else:
      self._recipient.sendMessage(message)

  def sendImage(self, imagePath):
    if self.isGroup():
      subprocess.call(["osascript", "sendpicgc.scpt", imagePath, "iMessage;+;" + self._roomname])
    else:
      subprocess.call(["osascript", "sendpic.scpt", imagePath, self._recipient.getId()])

  def __str__(self):
    return "Roomname: {0}, Recipient: {1}".format(self._roomname, self._recipient)

