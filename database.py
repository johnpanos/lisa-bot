import sqlite3

class Database:
  def __init__(self, path):
    self._db = sqlite3.connect(path)

  def getLastRowId(self):
    c = self._db.cursor()
    c.execute("SELECT ROWID FROM message ORDER BY ROWID DESC LIMIT 1")
    return c.fetchone()[0]

  def getMessageForRowId(self, rowid):
    c = self._db.cursor()
    c.execute("SELECT message.text, handle.id from message LEFT OUTER JOIN handle ON message.handle_id = handle.ROWID WHERE message.ROWID=?", (rowid, ))
    return c.fetchone()