import json
from imessage.buddy import Buddy

class AdminError(Exception):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

class RoleManager:
  def __init__(self):
    self.loadRoles()

  def loadRoles(self):
    roleFile = open("roles.json")
    self._roleDict = json.load(roleFile)
    roleFile.close()
  
  def getAdmins(self):
    return self._roleDict["admins"]

  def isAdmin(self, buddy):
    self._validateInput(buddy)
    return buddy.getId() in self.getAdmins()

  def ifNotAdminRaise(self, buddy):
    if not self.isAdmin(buddy):
      raise AdminError

  def _validateInput(self, buddy):
    if not isinstance(buddy, Buddy):
      raise ValueError

  def addAdmin(self, buddy):
    self._validateInput(buddy)
    self._roleDict["admins"].append(buddy.getId())
    self._save()

  def _save(self):
    roleFile = open("roles.json", "w")
    json.dump(self._roleDict, roleFile)
    roleFile.close()
