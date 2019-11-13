import subprocess
from imessage.contacts import getName

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