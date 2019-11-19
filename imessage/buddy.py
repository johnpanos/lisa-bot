import subprocess
from imessage.contacts import getName

class Buddy:
  def __init__(self, idA, name=None):
    self._id = idA
    self._name = self.getName()

  def getId(self):
    return self._id

  def getName(self):
    name = getName(self._id)
    if name is not None:
      return name
    else:
      return self._id

  def sendMessage(self, message):
    subprocess.call(["osascript", "send.scpt", message, self._id])

  def __repr__(self):
    mystring = (
      "ID: {0}\n"
      "Name: {1}\n"
    )
    return mystring.format(self.getId(), self.getName())