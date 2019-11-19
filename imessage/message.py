class Message:
  """Model class for Message"""
  def __init__(self, message, chat):
    self._text = message
    self._chat = chat

  def getText(self):
    """Returns: str"""
    return self._text

  def getChat(self):
    """
    Returns: Chat
    """
    return self._chat

  def __str__(self):
    return "Message: {0}\nChat: {1}".format(self._text, str(self._chat))