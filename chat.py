import subprocess

class Recipient:
  def __init__(self, idA, name="Name Not Found"):
    self._id = idA
    self._name = name

  def getId(self):
    return self._id

  def sendMessage(self, message):
    subprocess.call(["osascript", "send.scpt", message, self._id])

  def __str__(self):
    return "Id: {0}, Name: {1}".format(self._id, self._name)

class Chat:
  def __init__(self, recipient, roomname=None):
    self._roomname =  roomname
    if type(recipient) == str:
      self._recipient = Recipient(recipient)
    else:
      self._recipient = recipient

  def isGroup(self):
    return self._roomname is not None

  def sendMessage(self, message):
    if self.isGroup():
      subprocess.call(["osascript", "sendgc.scpt", message, "iMessage;+;" + self._roomname])
    else:
      self._recipient.sendMessage(message)

  def __str__(self):
    return "Roomname: {0}, Recipient: {1}".format(self._roomname, self._recipient)

