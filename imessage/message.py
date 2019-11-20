class Message:
  """Model class for Message"""
  def __init__(self, message, chat, buddy, subject=None):
    self._text = message
    self._subject = subject

    self._chat = chat

    self._buddy = buddy

  def getText(self):
    """Returns: str"""
    return self._text

  def getChat(self):
    """
    Returns: Chat
    """
    return self._chat

  def getSender(self):
    return self._buddy

  def __str__(self):
    return "Message: {0}\nChat: {1}".format(self._text, str(self._chat))