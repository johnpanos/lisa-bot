import subprocess
from imessage.recipient import Recipient

class Chat:
  def __init__(self, recipient, roomname=None):
    """Chat constructor!"""
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

