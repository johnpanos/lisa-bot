import subprocess
from imessage.buddy import Buddy
from database import db

class Chat:
  def __init__(self):
    pass

  def sendMessage(self, message):
    print("not implemented")

  def sendImage(self, imagePath):
    print("not implemented")

class BuddyChat(Chat):
  def __init__(self, buddy):
    if not isinstance(buddy, Buddy):
      raise ValueError("buddy must be of type Buddy")
    self._buddy = buddy

  def getBuddy(self):
    return self._buddy

  def sendMessage(self, message):
    self._buddy.sendMessage(message)
  
  def sendImage(self, imagePath):
    subprocess.call(["osascript", "sendpic.scpt", imagePath, self._buddy.getId()])

class GroupChat(Chat):
  def __init__(self, roomName=None, displayName="N/A"):
    self._roomName = roomName
    self._displayName = displayName
    self._members = None

  def sendMessage(self, message):
    subprocess.call(["osascript", "sendgc.scpt", message, self.getGuid()])

  def sendImage(self, imagePath):
    subprocess.call(["osascript", "sendpicgc.scpt", imagePath, self.getGuid()])
  
  def getRoomName(self):
    return self._roomName

  def getDisplayName(self):
    if self._displayName == "N/A":
      c = db.getCursor()
      c.execute("SELECT chat.display_name FROM chat WHERE chat.room_name = ?", (self.getRoomName(), ))
      self._displayName = c.fetchone()[0] or "N/A"
    return self._displayName

  def getGuid(self):
    return "iMessage;+;" + self._roomName

  def getMembers(self):
    if self._members is None:
      self._members = []
      c = db.getCursor()
      query = (
        "SELECT handle.id FROM chat"
        " LEFT OUTER JOIN chat_handle_join ON chat.ROWID = chat_handle_join.chat_id"
        " LEFT OUTER JOIN handle ON handle.ROWID = chat_handle_join.handle_id"
        " WHERE chat.guid = ?;"
      )
      rows = c.execute(query, (self.getGuid(), )).fetchall()
      for row in rows:
        self._members.append(Buddy(row[0]))
    return self._members

  def __repr__(self):
    mystring = (
      "Display Name: {0}\n"
      "GUID: {1}\n"
      "Roomname: {2}\n"
      "Members: \n\t{3}\n"
    )
    return mystring.format(self.getDisplayName(), self.getGuid(), self.getRoomName(), "\n\t".join([str(b).replace("\n", "\n\t") for b in self.getMembers()]))

  def __str__(self):
    return self.__repr__()