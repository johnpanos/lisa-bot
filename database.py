import sqlite3

class Database:
  def __init__(self, path):
    self._db = sqlite3.connect(path)

  def getLastRowId(self):
    c = self._db.cursor()
    c.execute("SELECT * FROM message WHERE message.is_from_me = 0 AND message.text IS NOT NULL ORDER BY message.ROWID DESC LIMIT 1;")
    return c.fetchone()[0]

  def getMessageForRowId(self, rowid):
    c = self._db.cursor()
    c.execute("SELECT message.text, message.cache_roomnames, handle.id from message LEFT OUTER JOIN handle ON message.handle_id = handle.ROWID WHERE message.ROWID=?", (rowid, ))
    return c.fetchone()

  def getCountForWord(self, chat, word):
    c = self._db.cursor()
    c.execute("SELECT COUNT(message.text), handle.id FROM message LEFT OUTER JOIN handle ON message.handle_id = handle.ROWID WHERE message.is_from_me = 0 AND message.cache_roomnames = ? AND message.text LIKE ? GROUP BY message.handle_id", (chat.getRoomname(), "%" + word + "%", ))
    print(c)
    return c.fetchall()

db = Database("/Users/john/Library/Messages/chat.db")