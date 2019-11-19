import sqlite3

class Database:
  def __init__(self, path):
    self._db = sqlite3.connect(path)

  def getLastRowId(self, prevRowId=None):
    c = self._db.cursor()
    if prevRowId is None:
      return c.execute("SELECT * FROM message WHERE message.is_from_me = 0 AND message.text IS NOT NULL ORDER BY message.ROWID DESC LIMIT 1;").fetchone()[0]
    else:
      return c.execute("SELECT message.ROWID, message.text, message.cache_roomnames, handle.id from message LEFT OUTER JOIN handle ON message.handle_id = handle.ROWID WHERE message.ROWID > ?", (prevRowId, ))

  def getMessageForRowId(self, rowid):
    c = self._db.cursor()
    c.execute("SELECT message.text, message.cache_roomnames, handle.id from message LEFT OUTER JOIN handle ON message.handle_id = handle.ROWID WHERE message.ROWID=?", (rowid, ))
    return c.fetchone()

  def getCountForWord(self, chat, word):
    c = self._db.cursor()
    c.execute("SELECT COUNT(message.text), handle.id FROM message LEFT OUTER JOIN handle ON message.handle_id = handle.ROWID WHERE message.is_from_me = 0 AND message.cache_roomnames = ? AND message.text LIKE ? AND message.text NOT LIKE '%wordstat%' GROUP BY message.handle_id", (chat.getRoomName(), "%" + word + "%", ))
    print(c)
    return c.fetchall()

  def getCursor(self):
    return self._db.cursor()

db = Database("/Users/panos/Library/Messages/chat.db")